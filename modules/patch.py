import os.path

dotaHeroes = ["Anti-Mage", "Axe", "Bane", "Bloodseeker", "Crystal Maiden", "Drow Ranger", "Earthshaker", "Juggernaut", "Mirana", "Shadow Fiend", "Morphling", "Phantom Lancer", "Puck", "Pudge", "Razor", "Sand King", "Storm Spirit", "Sven", "Tiny", "Vengeful Spirit", "Windranger", "Zeus", "Kunkka", "Lina", "Lich", "Lion", "Shadow Shaman", "Slardar", "Tidehunter", "Witch Doctor", "Riki", "Enigma", "Tinker", "Sniper", "Necrophos", "Warlock", "Beastmaster", "Queen of Pain", "Venomancer", "Faceless Void", "Wraith King", "Death Prophet", "Phantom Assassin", "Pugna", "Templar Assassin", "Viper", "Luna", "Dragon Knight", "Dazzle", "Clockwerk", "Leshrac", "Nature's Prophet", "Lifestealer", "Dark Seer", "Clinkz", "Omniknight", "Enchantress", "Huskar", "Night Stalker", "Broodmother", "Bounty Hunter", "Weaver", "Jakiro", "Batrider", "Chen", "Spectre", "Doom", "Ancient Apparition", "Ursa", "Spirit Breaker", "Spiritbreaker", "Gyrocopter", "Alchemist", "Invoker", "Silencer", "Outworld Devourer", "Lycan", "Brewmaster", "Shadow Demon", "Lone Druid", "Chaos Knight", "Meepo", "Treant Protector", "Ogre Magi", "Undying", "Rubick", "Disruptor", "Nyx Assassin", "Naga Siren", "Keeper of the Light", "Io", "Wisp", "Visage", "Slark", "Medusa", "Troll Warlord", "Centaur Warrunner", "Centaur", "Magnus", "Timbersaw", "Bristleback", "Tusk", "Skywrath Mage", "Skywrath mage", "Abaddon", "Elder Titan", "Legion Commander", "Ember Spirit", "Earth Spirit", "Earth spirit", "Terrorblade", "Phoenix", "Oracle", "Techies", "Winter Wyvern", "Arc Warden", "Underlord"]
dotaItems = ["Blink Dagger", "Blades of Attack", "Broadsword", "Chainmail", "Claymore", "Helm of Iron Will", "Javelin", "Mithril Hammer", "Platemail", "Quarterstaff", "Quelling Blade", "Faerie Fire", "Infused Raindrop", "Wind Lace", "Ring of Protection", "Stout Shield", "Recipe: Moon Shard", "Moon Shard", "Gauntlets of Strength", "Slippers of Agility", "Mantle of Intelligence", "Iron Branch", "Belt of Strength", "Band of Elvenskin", "Robe of the Magi", "Circlet", "Ogre Club", "Blade of Alacrity", "Staff of Wizardry", "Ultimate Orb", "Gloves of Haste", "Morbid Mask", "Ring of Regen", "Sage's Mask", "Boots of Speed", "Gem of True Sight", "Cloak", "Talisman of Evasion", "Cheese", "Magic Stick", "Recipe: Magic Wand", "Magic Wand", "Ghost Scepter", "Clarity", "Enchanted Mango", "Healing Salve", "Dust of Appearance", "Bottle", "Observer Ward", "Sentry Ward", "Recipe: Observer and Sentry Wards", "Observer and Sentry Wards", "Tango", "Tango (Shared)", "Animal Courier", "Town Portal Scroll", "Recipe: Boots of Travel", "Recipe: Boots of Travel", "Boots of Travel", "Boots of Travel", "Recipe: Phase Boots", "Phase Boots", "Demon Edge", "Eaglesong", "Reaver", "Sacred Relic", "Hyperstone", "Ring of Health", "Void Stone", "Mystic Staff", "Energy Booster", "Point Booster", "Vitality Booster", "Recipe: Power Treads", "Power Treads", "Recipe: Hand of Midas", "Hand of Midas", "Recipe: Oblivion Staff", "Oblivion Staff", "Recipe: Perseverance", "Perseverance", "Recipe: Poor Man's Shield", "Poor Man's Shield", "Recipe: Bracer", "Bracer", "Banana", "Recipe: Wraith Band", "Wraith Band", "Recipe: Null Talisman", "Null Talisman", "Recipe: Mekansm", "Mekansm", "Recipe: Vladmir's Offering", "Vladmir's Offering", "Flying Courier", "Recipe: Buckler", "Buckler", "Recipe: Ring of Basilius", "Ring of Basilius", "Recipe: Pipe of Insight", "Pipe of Insight", "Recipe: Urn of Shadows", "Urn of Shadows", "Recipe: Headdress", "Headdress", "Recipe: Scythe of Vyse", "Scythe of Vyse", "Recipe: Orchid Malevolence", "Orchid Malevolence", "Recipe: Bloodthorn", "Bloodthorn", "Recipe: Echo Sabre", "Echo Sabre", "Recipe: Eul's Scepter of Divinity", "Eul's Scepter of Divinity", "Recipe: Aether Lens", "Aether Lens", "Recipe: Force Staff", "Force Staff", "Recipe: Hurricane Pike", "Hurricane Pike", "Recipe: Dagon", "Recipe: Dagon", "Recipe: Dagon", "Recipe: Dagon", "Recipe: Dagon", "Dagon", "Dagon", "Dagon", "Dagon", "Dagon", "Recipe: Necronomicon", "Recipe: Necronomicon", "Recipe: Necronomicon", "Necronomicon", "Necronomicon", "Necronomicon", "Recipe: Aghanim's Scepter", "Aghanim's Scepter", "Recipe: Refresher Orb", "Refresher Orb", "Recipe: Assault Cuirass", "Assault Cuirass", "Recipe: Heart of Tarrasque", "Heart of Tarrasque", "Recipe: Black King Bar", "Black King Bar", "Aegis of the Immortal", "Recipe: Shiva's Guard", "Shiva's Guard", "Recipe: Bloodstone", "Bloodstone", "Recipe: Linken's Sphere", "Linken's Sphere", "Recipe: Lotus Orb", "Lotus Orb", "Recipe: Vanguard", "Vanguard", "Recipe: Crimson Guard", "Crimson Guard", "Recipe: Blade Mail", "Blade Mail", "Recipe: Soul Booster", "Soul Booster", "Recipe: Hood of Defiance", "Hood of Defiance", "Recipe: Divine Rapier", "Divine Rapier", "Recipe: Monkey King Bar", "Monkey King Bar", "Recipe: Radiance", "Radiance", "Recipe: Butterfly", "Butterfly", "Recipe: Daedalus", "Daedalus", "Recipe: Skull Basher", "Skull Basher", "Recipe: Battle Fury", "Battle Fury", "Recipe: Manta Style", "Manta Style", "Recipe: Crystalys", "Crystalys", "Recipe: Dragon Lance", "Dragon Lance", "Recipe: Armlet of Mordiggian", "Armlet of Mordiggian", "Armlet", "Recipe: Shadow Blade", "Shadow Blade", "Recipe: Silver Edge", "Silver Edge", "Recipe: Sange and Yasha", "Sange and Yasha", "Recipe: Satanic", "Satanic", "Recipe: Mjollnir", "Mjollnir", "Recipe: Eye of Skadi", "Eye of Skadi", "Recipe: Sange", "Sange", "Recipe: Helm of the Dominator", "Helm of the Dominator", "Recipe: Maelstrom", "Maelstrom", "Recipe: Desolator", "Desolator", "Recipe: Yasha", "Yasha", "Recipe: Mask of Madness", "Mask of Madness", "Recipe: Diffusal Blade", "Recipe: Diffusal Blade", "Diffusal Blade", "Diffusal Blade", "Recipe: Ethereal Blade", "Ethereal Blade", "Recipe: Soul Ring", "Soul Ring", "Recipe: Arcane Boots", "Arcane Boots", "Recipe: Octarine Core", "Octarine Core", "Orb of Venom", "Blight Stone", "Recipe: Drum of Endurance", "Drum of Endurance", "Recipe: Medallion of Courage", "Medallion of Courage", "Recipe: Solar Crest", "Solar Crest", "Smoke of Deceit", "Tome of Knowledge", "Recipe: Veil of Discord", "Veil of Discord", "Recipe: Guardian Greaves", "Guardian Greaves", "Recipe: Rod of Atos", "Rod of Atos", "Recipe: Iron Talon", "Iron Talon", "Recipe: Abyssal Blade", "Abyssal Blade", "Recipe: Heaven's Halberd", "Heaven's Halberd", "Recipe: Ring of Aquila", "Ring of Aquila", "Recipe: Tranquil Boots", "Tranquil Boots", "Shadow Amulet", "Recipe: Glimmer Cape", "Glimmer Cape", "Greevil Taffy", "DOTA_Tooltip_Ability_item_mystery_hook", "DOTA_Tooltip_Ability_item_mystery_arrow", "DOTA_Tooltip_Ability_item_mystery_missile", "DOTA_Tooltip_Ability_item_mystery_toss", "DOTA_Tooltip_Ability_item_mystery_vacuum", "DOTA_Tooltip_Ability_item_halloween_rapier", "Greevil Whistle", "Greevil Whistle", "A Gift!", "Xmas Stocking", "Speed Skates", "Fruit-bit Cake", "Wizard Cookie", "Cocoa with Marshmallows", "Clove Studded Ham", "Kringle", "Snow Mushroom", "Greevil Treat", "Greevil Chow", "Greevil Blink Bone", "River Vial: Chrome", "River Vial: Dry", "River Vial: Slime", "River Vial: Oil", "River Vial: Electrified", "River Vial: Potion", "River Vial: Blood"]


def formatNotes(notes, game):
	if game == "dota":
		prettytext = list(filter(None, notes.strip().split("\n")))
		prettytext = [x.strip() for x in prettytext]
		textBuilder = []
		inList = False
		changeList = []
		for line in prettytext:
			formattedLine = line
			if inList == False and line[0] == "*":
				inList=True
				formattedLine=">```"+line[1:]+"\n"
			elif inList == True:
				if line[0] == "*":
					formattedLine = line[1:]+"\n"
				else:
					inList=False
					if line == "HEROES" or line == "ITEMS":
						formattedLine = "```\n\n*"+line+"*\n"
					elif line in dotaHeroes or line in dotaItems:
						formattedLine = "```\n_"+line+"_\n"
			elif "Gameplay Update" in line:
				formattedLine = "*_"+line+"_*\n"
			elif line == "HEROES" or line == "ITEMS":
				formattedLine = "\n*"+line+"*\n"
			elif line in dotaHeroes or line in dotaItems:
				formattedLine = "_"+line+"_\n"

			textBuilder.append(formattedLine)
		if inList:
			textBuilder.append("```")
		prettytext="".join(textBuilder)
		return prettytext
	else:
		return notes;

def patchFetch(args, slackAPI, channel):
	if len(args)==0:
		return "EE: patch: not enough arguments"
	datfile = "/etc/slackbot/modules/patch/"+args[0]
	if os.path.isfile(datfile):
		patchnotes=open('/etc/slackbot/modules/patch/'+args[0]).read()
		formattedText = formatNotes(patchnotes, args[0])
		slackAPI.chat.post_message(channel['name'], formattedText, as_user=True, username="patchbot")
		return "II: patch: posted patch notes for "+args[0]
	slackAPI.chat.post_message(channel['name'], "Couldn't find patch notes for '"+args[0]+"'. Either this isn't a real game or @roogz is fucking memeing again.")
	return "EE: patch: patch notes not found for "+args[0]

