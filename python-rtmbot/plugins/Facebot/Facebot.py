#!/usr/bin/env python3
import threading
import re
import json
import logging
#import /var/www/slackbot/modules/baseModule
from slacker import Slacker

facebook='C1X835M9U'
facebookGroupId='991923644160943'
appId='1153514404690882'
facebookLoginUrl='https://www.facebook.com/dialog/oauth?client_id={}&redirect_uri={}'



import requests
from facebot import Facebook
from facebot.message import send_group
#import request

logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)
crontable = []
outputs = []

with open("/etc/slackbot/Facebot") as f:
	content = f.readlines()

USERNAME = content[0]
PASSWORD = content[1]
fb = Facebook(USERNAME, PASSWORD)
log.info('login %s', fb.user_id)
secret = str(open('/etc/slackbot/API').read().strip())
slack = Slacker(secret)
#slack.channels.history("#facebook")
#slack.chat.post_message("#general", "test")

def get_sticky():
    '''
    Call pull api to get sticky and pool parameter,
    newer api needs these parameter to work.
    '''
    url = 'https://0-edge-chat.facebook.com/pull?channel=p_{user_id}&partition=-2&clientid=3396bf29&cb=gr6l&idle=0&cap=8&msgs_recv=0&uid={user_id}&viewer_uid={user_id}&state=active&seq=0'

    # call pull api, and set timeout as one minute
    res = fb.session.get(url.format(user_id=fb.user_id), timeout=60)

    # remove for (;;); so we can turn them into dictionaries
    content = json.loads(re.sub('for \(;;\); ', '', res.text))

    # check existence of lb_info
    if 'lb_info' not in content:
        raise Exception('Get sticky pool error')

    sticky = content['lb_info']['sticky']
    pool = content['lb_info']['pool']

    return sticky, pool

def get_user_by_id(uid):
    url = 'https://graph.facebook.com/v2.7/' + uid + '?access_token=' + fb.get_access_token() + '&debug=all&format=json&method=get&pretty=0&suppress_http_code=1'
    content = (str(requests.get(url).content))
    content = (content.replace('b\'', '').replace('\'', ''))
    content = json.loads(re.sub('for \(;;\); ;', '', content))
    print(content)
    return content['name']


def pull_message(sticky, pool, seq='0'):
    '''
    Call pull api with seq value to get message data.
    '''
    url = 'https://0-edge-chat.facebook.com/pull?channel=p_{user_id}&partition=-2&clientid=3396bf29&cb=gr6l&idle=0&cap=8&msgs_recv=0&uid={user_id}&viewer_uid={user_id}&state=active&seq={seq}&sticky_token={sticky}&sticky_pool={pool}'

    # call pull api, and set timeout as one minute
    res = fb.session.get(
        url.format(user_id=fb.user_id, seq=seq, sticky=sticky, pool=pool),
        timeout=60)

    log.debug(res.text)
    # remove for (;;); so we can turn them into dictionaries
    content = json.loads(re.sub('for \(;;\); ', '', res.text))


    # get seq from response
    seq = content.get('seq', '0')
    log.debug('seq: %s', seq)

    return content, seq


def get_message(content):
    '''
    Get message and author name from content.
    May contains multiple messages in the content.
    '''
    if 'ms' not in content:
        return

    for m in content['ms']:
        # we only want item which type is m_messaging
        if m.get('type') != 'delta':
            continue
        try:
            m = m['delta']
            print(m)
            message = m['body']
            #print(message)
            author_id = m['messageMetadata']['actorFbId']
            #print(author_id)
            try:
                author_name = get_user_by_id(author_id)
            except Exception:
                print("Cant get username")
                author_name = author_id
            #print(author_name)
            tid = m['messageMetadata']['threadKey']['threadFbId']
            #print(tid)
            yield tid, author_id, author_name, message
        except KeyError:
            print("Cant parse message")
            return

def get_fb_channel():
	for channel in slack.channels.list().body['channels']:
		if(channel['name'] == 'facebook'):
			return channel['id']
	return ""


def main():
    # get sticky and pool parameter, so we can listener for message
    sticky, pool = get_sticky()

    # call pull api without seq, so we can get seq value from response
    _, seq = pull_message(sticky, pool)

    fb_channel = get_fb_channel()

    while True:
        # tell facebook that client is alive
        fb.ping()

        # call pull api with seq
        try:
            content, seq = pull_message(sticky, pool, seq)
        except requests.exceptions.RequestException as e:
            log.warn('RequestException: {}'.format(e))
            continue

        # iterate through each message in response
        for tid, author_id, author_name, message in get_message(content):
            log.debug('%s(%s): %s', author_id, message)
            #print(message, author_id)
            #print(tid)

            # if author is myself, leave him alone
            if not tid == '991923644160943':
              continue


            if tid.startswith('mid'):
                # this was sent from person
                log.info('%s: %s', author_id, message)
            elif tid.startswith('id'):
                # this was sent from group
                log.info('%s: %s', tid[3:], message)
            print(slack.chat.post_message('#facebook', author_name + ': ' +  message))

        #print(slack.channels.history(fb_channel, unreads=1).body)

def process_message(data):
	if data['channel'] == facebook:
		fb.send_group('991923644160943', data['message'])

#fb.get_access_token()

#if __name__ == '__main__':
t1 = threading.Thread(target=main)
t1.start()
t1.join()
