# Made by Hydrovolter#8432
#
#
# Import Modules

import random
import time

print("Made by Hydrovolter#8432\n\n")

# Global Variables

playerName = "Player" # Default

STR = 0
DEX = 0
CON = 0
WIS = 0
INT = 0
CHA = 0

# armour = 1
race = ""
Class = ""

xp = 0
lastLevel = 0
# xp = add_xp(xp, 1000)
# print("Player is now level", get_level(xp)) # Output: Player is now level 3

canPlayLuckyDice = True



# Dice Rolls

def d4():
    d4roll = random.randint(1,4)
    return d4roll
def d6():
    d6roll = random.randint(1,6)
    return d6roll
def d8():
    d8roll = random.randint(1,8)
    return d8roll
def d10():
    d10roll = random.randint(1,10)
    return d10roll
def d12():
    d12roll = random.randint(1,12)
    return d12roll
def d20():
    d20roll = random.randint(1,20)
    return d20roll
def d100():
    d100tens = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    d100units = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    d100rolltens = random.choice(d100tens)
    d100rollunits = random.choice(d100units)
    d100roll = d100rolltens + d100rollunits
    if d100roll == 0:
        d100roll = 100
    return d100roll

# XP System

def add_xp(player_xp, xp_to_add):
    player_xp += xp_to_add
    return player_xp
def get_level(player_xp):
    # DND XP System
    xp_thresholds = [0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000]
    # for i in range(len(xp_thresholds)):
    #     if player_xp < xp_thresholds[i]:
    #         return i-1
    # return 20
    for i, threshold in enumerate(xp_thresholds):
        if player_xp < threshold:
            return i - 1
    return 20

# Action Panel System

class Character:
    def __init__(self, name, hp, damage, armor):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.armor = armor
class ActionPanel:
    def __init__(self, character):
        self.character = character

    def attack(self, target):
        damage = random.randint(self.character.damage//2, self.character.damage)
        total_damage = damage - target.armor
        if total_damage <= 0:
            print(f"\n{target.name} blocks the attack!")
        else:
            target.hp -= total_damage
            print(f"\n{self.character.name} attacks {target.name} for {total_damage} damage!")
            if target.hp <= 0:
                print(f"\n{target.name} has been defeated!")
                return "defeat"

    def defend(self):
        if self.character.armor <= 5: self.character.armor += 1

        print(f"\n{self.character.name} prepares to defend!")

    def heal(self):
        heal_amount = random.randint(1, 10)
        self.character.hp += heal_amount
        print(f"\n{self.character.name} heals for {heal_amount} hp!")

    # self, name, hp, damage, armor
    # player = Character("Player", 50, 10, 5)
    # enemy = Character("Goblin", 30, 5, 2)

    # player_actions = ActionPanel(player)
    # enemy_actions = ActionPanel(enemy)

    # player_actions.attack(enemy)
    # enemy_actions.defend()
    # player_actions.attack(enemy)
    # enemy_actions.attack(player)
    # player_actions.heal()

def battle_choice():
    options = ["Attack", "Defend", "Heal"]
    print("\nChoose your battle strategy:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    try:
        choice = int(input("Enter your choice (1-3): "))
    except:
        print("Invalid choice! Please choose again.")
        return battle_choice()
    if choice == 1:
        return "attack"
    elif choice == 2:
        return "defend"
    elif choice == 3:
        return "heal"
    else:
        print("Invalid choice! Please choose again.")
        return battle_choice()

# Create Character

def createCharacter(character_name):
    global STR, DEX, CON, WIS, INT, CHA
    # global race
    # global Class
    # global xp

    # Abilities
    print("\nAbilities:\n\nStrength (STR)\nDexterity (DEX)\nConstitution (CON)\nWisdom (WIS)\nIntelligence (INT)\nCharisma (CHA)\n")
    abilities = ["STR", "DEX", "CON", "WIS", "INT", "CHA"]
    scores = [15, 14, 13, 12, 10, 8]

    for _, score in enumerate(scores):
        ability = None
        while ability not in abilities:
            num = score
            ability = input(f"Choose an ability to be score {num} (Use shortened version): ")
            ability = ability.upper()

            if ability in abilities:
                if globals()[ability] == 0:
                    globals()[ability] = num
                    break
                else:
                    print("You cannot choose an ability you have already chosen!")
                    ability = None
            else:
                print("Please enter a valid ability")

    print("\nAbility Stats:\n")
    print(f"Name: {character_name}")
    print("Strength: " + str(STR))
    print("Dexterity: " + str(DEX))
    print("Constitution: " + str(CON))
    print("Wisdom: " + str(WIS))
    print("Intelligence: " + str(INT))
    print("Charisma: " + str(CHA))


    # Race
    races = ["human", "elf", "dwarf", "half-orc", "tiefling", "half-elf", "dragonborn", "gnome", "halfling"] # added from dwarf [3]
    print("\nRaces:\n\nHuman\nElf\nDwarf\n")
    global race
    race = None
    while race not in races:
        num = 15
        race = input("Choose a race: ")
        racelowered = race.lower()
        if racelowered in races:
            race = racelowered
            if racelowered == "human":
                STR += 1
                DEX += 1
                CON += 1
                WIS += 1
                INT += 1
                CHA += 1
            elif racelowered == "elf":
                DEX += 2
                WIS += 2
            elif racelowered == "dwarf":
                STR += 1
                CON += 2
            elif racelowered == "half-orc": # added from here
                STR += 2
                CON += 1
            elif racelowered == "tiefling":
                INT += 1
                CHA += 2
            elif racelowered == "half-elf":
                INT += 1
                CHA += 2
            elif racelowered == "dragonborn":
                STR += 2
                CHA += 1
            elif racelowered == "gnome":
                INT += 2
                DEX += 1
            elif racelowered == "halfling":
                DEX += 2
                CON += 1
            break
        else:
            print("Please enter a valid race")

    print("\nUpdated Ability Stats:\n")
    print(f"Name: {character_name}")
    print("Strength: " + str(STR))
    print("Dexterity: " + str(DEX))
    print("Constitution: " + str(CON))
    print("Wisdom: " + str(WIS))
    print("Intelligence: " + str(INT))
    print("Charisma: " + str(CHA))
    print(f"Race: {race.capitalize()}")

    # Class
    classes = ["fighter", "wizard", "monk"]
    print("\nClasses:\n\nFighter\nWizard\nMonk")
    global Class
    Class = None
    while Class not in classes:
        num = 15
        Class = input("\nChoose a class: ")
        classlowered = Class.lower()
        if classlowered in classes:
            if classlowered == "fighter":
                print("Fighters are profecient with weapons, and are natural leaders, with good constitution. +2 STR, +2 CHA, and +1 CON. However, they aren't the smartest of creatures. -2 INT, -1 WIS")
                Class = "fighter"
                STR += 2
                CHA += 2
                CON += 1
                INT -= 2
                WIS -= 1
            elif classlowered == "wizard":
                print("Wizards are quite smart, being able to memorise and perform a variety of spells. +2 INT, +2 WIS, +1 DEX. However, they aren't natural leaders or have combat prowess. -2 CHA, -1 STR")
                Class = "wizard"
                INT += 2
                WIS += 2
                DEX += 1
                CHA -= 2
                STR -= 1
            elif classlowered == "monk":
                print("Monks are agile and fast, specialising in unarmed combat, so their body can naturally take more of a 'punch'. +2 DEX, +2 CON, +1 STR. However, they struggle in social aspects of life. -2 WIS, -1 INT ")
                Class = "monk"
                DEX += 2
                CON += 2
                STR += 1
                WIS -= 2
                INT -= 1
            break
        else:
            print("Please enter a valid race")

    print("\nUpdated Ability Stats:\n")
    print(f"Name: {character_name}")
    print("Strength: " + str(STR))
    print("Dexterity: " + str(DEX))
    print("Constitution: " + str(CON))
    print("Wisdom: " + str(WIS))
    print("Intelligence: " + str(INT))
    print("Charisma: " + str(CHA))
    print(f"Race: {race.capitalize()}")
    print(f"Class: {Class.capitalize()}")

# Create Setting

def createSetting():
    settingRoll = d4()
    print("\nRolling the D4 dice to choose the setting for this adventure...")
    time.sleep(3)
    print(f"You rolled a... {str(settingRoll)}!\n")
    time.sleep(1)
    if settingRoll == 1:
        print("As the storm raged on outside, thunderous crashes reverberated through the night sky, accompanied by a downpour of rain that seemed never-ending. The darkness outside was only interrupted by occasional flashes of lightning, illuminating the small village and the lonely pub that sat at its center. Despite the chaos of the storm, the warm and inviting light of the pub shone brightly, beckoning those seeking refuge from the elements. Inside, the atmosphere was lively and energetic, with a group of tipsy patrons cheering and laughing, oblivious to the tempest outside. Amidst the sounds of glasses clinking and raucous chatter, the booming sound of the thunder was like a wild drumbeat, adding to the cacophony of the night.")
    elif settingRoll == 2:
        print("As the sun slowly sets outside, casting a warm, golden glow across the sky, the cosy house seems to come alive with a sense of comfort and tranquility. Inside, the soft glow of lamps and flickering candles fills the rooms with a warm, inviting ambiance.\nThe crackling of logs in the fireplace, coupled with the subtle aroma of woodsmoke, adds to the cozy atmosphere. Plush cushions and soft blankets are scattered throughout the living room, inviting you to snuggle up and get comfortable. The walls are adorned with warm, earthy colors and tasteful decor, creating a sense of calm and relaxation.\nAs the evening draws in and the stars twinkle in the sky, the warm embrace of the house seems to wrap around you, inviting you to stay a little longer and soak in the peacefulness of the moment.")
    elif settingRoll == 3:
        print("Nestled deep in the heart of a wet, swampy green forest stands a magnificent tree house, a verdant oasis rising above the damp ground. The forest canopy envelops the tree house in a cloak of green, while vines and leaves drape themselves over the wooden beams, as if nature itself has woven a protective veil around it. The tree house appears to have grown organically out of the tree, with its wooden planks twisting and turning to match the shape of the trunk. A rickety wooden ladder leads up to the small, but cozy interior, where the smell of fresh wood mingles with the earthy scent of the surrounding forest. From the windows, one can catch glimpses of the misty, swampy landscape stretching out as far as the eye can see, while the gentle creaking of the tree house lends a soothing rhythm to the tranquil sounds of the forest.")
    elif settingRoll == 4:
        print("Amidst the chaotic buzz of an urban jungle, the skyscraper stands tall and proud, a modern marvel of architectural engineering. Its smooth glass and steel facade reflects the hustle and bustle of the city below, with streams of cars and people flowing like rivers around its base. As one gazes upwards, the tower seems to reach endlessly into the sky, disappearing into the clouds above. From within, the views are breathtaking, as the cityscape spreads out in all directions, a sprawling metropolis of concrete and steel. The constant hum of traffic and the distant sounds of honking horns permeate the air, serving as a constant reminder of the frenetic energy of the city that never sleeps.")
    time.sleep(5)

# Check Level

def checkLevel():
    global STR, DEX, INT, CON, lastLevel

    # lastLevel = get_level(xp)
    if get_level(xp) > lastLevel:
        print(f"Congratulations! You levelled up! Your current level is: {str(get_level(xp))}")
        print("Levelling up grants you benefits depending on your class! You have a 1/2 chance of gaining +1 CON or +1 STR, INT, or DEX.")
        if Class == "fighter":
            randomint = random.randint(1,2) # 1 = STR, 2 = CON
            ablAddName = ""
            if randomint == 1:
                STR += 1
                ablAddName = "STR"
            else:
                CON += 1
                ablAddName = "CON"
            print(f"As you are in the fighter class, you gain +1 {ablAddName}")
        elif Class == "wizard":
            randomint = random.randint(1,2) # 1 = INT, 2 = CON
            ablAddName = ""
            if randomint == 1:
                INT += 1
                ablAddName = "INT"
            else:
                CON += 1
                ablAddName = "CON"
            print(f"As you are in the wizard class, you gain +1 {ablAddName}")
        elif Class == "monk":
            randomint = random.randint(1,2) # 1 = DEX, 2 = CON
            ablAddName = ""
            if randomint == 1:
                DEX += 1
                ablAddName = "DEX"
            else:
                CON += 1
                ablAddName = "CON"
            print(f"As you are in the monk class, you gain +1 {ablAddName}")
        time.sleep(1)
    lastLevel = get_level(xp)

# Display Stats

def displayStats(character_name):
    print("\nUpdated Ability Stats:\n")
    print(f"Name: {character_name}")
    print("Strength: " + str(STR))
    print("Dexterity: " + str(DEX))
    print("Constitution: " + str(CON))
    print("Wisdom: " + str(WIS))
    print("Intelligence: " + str(INT))
    print("Charisma: " + str(CHA))
    print(f"Race: {race.capitalize()}")
    print(f"Class: {Class.capitalize()}")

# Dice Luck Game

def diceLuck():
    options = ["Play the Lucky Dice game", "Exit the Lucky Dice Game"]
    print("\nWould you like to:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    try:
        choice = int(input("Enter your choice (1, or 2): "))
    except:
        print("Invalid choice! Please choose again.")
        return diceLuck()
    if choice == 1:
        print("Okay, let's play!")
        time.sleep(1)
        playDiceLuck()

    elif choice == 2:
        print("Okay, returning to break menu!")
        breakOption()
    else:
        print("Invalid choice! Please choose again.")
        return diceLuck()

def playDiceLuck():
    global STR, DEX, CON, WIS, INT, CHA, canPlayLuckyDice
    abilities = ["STR", "DEX", "CON", "WIS", "INT", "CHA"]

    # Round 1

    r1 = d6()
    print("Round 1: You roll a...")
    time.sleep(1)
    print(f"{str(r1)}!")
    if r1 >= 3:
        print("Congratulations! You won!")

        ability = None
        while ability not in abilities:
            ability = input("Please pick an ability to add +1 to! (STR, DEX, CON, WIS, INT, CHA): ")
            abilityupped = ability.upper()
            if abilityupped in abilities:
                if abilityupped == "STR":
                    STR += 1
                elif abilityupped == "DEX":
                    DEX += 1
                elif abilityupped == "CON":
                    CON += 1
                elif abilityupped == "WIS":
                    WIS += 1
                elif abilityupped == "INT":
                    INT += 1
                elif abilityupped == "CHA":
                    CHA += 1
                break
            else:
                print("Please enter a valid ability")
    else:
        notZero = True
        while notZero is True:
            abilitydeducted = random.choice(abilities)
            if abilitydeducted == "STR":
                if STR != 0:
                    STR -= 1
                    notZero = False
            elif abilitydeducted == "DEX":
                if DEX != 0:
                    DEX -= 1
                    notZero = False
            elif abilitydeducted == "CON":
                if CON != 0:
                    CON -= 1
                    notZero = False
            elif abilitydeducted == "WIS":
                if WIS != 0:
                    WIS -= 1
                    notZero = False
            elif abilitydeducted == "INT":
                if INT != 0:
                    INT -= 1
                    notZero = False
            elif abilitydeducted == "CHA":
                if CHA != 0:
                    CHA -= 1
                    notZero = False
            print(f"Unfortunately, you lost. -1 will be deducted from a random ability. The ability chosen is: {abilitydeducted}")

        # Round 2

    r2 = d20()
    print("Round 2: You roll a...")
    time.sleep(1)
    print(f"{str(r2)}!")
    if r2 >= 10:
        print("Congratulations! You won!")

        ability = None
        while ability not in abilities:
            ability = input("Please pick an ability to add +1 to! (STR, DEX, CON, WIS, INT, CHA): ")
            abilityupped = ability.upper()
            if abilityupped in abilities:
                if abilityupped == "STR":
                    STR += 1
                elif abilityupped == "DEX":
                    DEX += 1
                elif abilityupped == "CON":
                    CON += 1
                elif abilityupped == "WIS":
                    WIS += 1
                elif abilityupped == "INT":
                    INT += 1
                elif abilityupped == "CHA":
                    CHA += 1
                break
            else:
                print("Please enter a valid ability")
    else:
        notZero = True
        while notZero is True:
            abilitydeducted = random.choice(abilities)
            if abilitydeducted == "STR":
                if STR != 0:
                    STR -= 1
                    notZero = False
            elif abilitydeducted == "DEX":
                if DEX != 0:
                    DEX -= 1
                    notZero = False
            elif abilitydeducted == "CON":
                if CON != 0:
                    CON -= 1
                    notZero = False
            elif abilitydeducted == "WIS":
                if WIS != 0:
                    WIS -= 1
                    notZero = False
            elif abilitydeducted == "INT":
                if INT != 0:
                    INT -= 1
                    notZero = False
            elif abilitydeducted == "CHA":
                if CHA != 0:
                    CHA -= 1
                    notZero = False
            print(f"Unfortunately, you lost. -1 will be deducted from a random ability. The ability chosen is: {abilitydeducted}")

    # Round 3

    r3 = d100()
    print("Round 3 (Final Round): You roll a...")
    time.sleep(1)
    print(f"{str(r3)}!")
    if r3 >= 50:
        print("Congratulations! You won!")

        ability = None
        while ability not in abilities:
            ability = input("Please pick an ability to add +1 to! (STR, DEX, CON, WIS, INT, CHA): ")
            abilityupped = ability.upper()
            if abilityupped in abilities:
                if abilityupped == "STR":
                    STR += 1
                elif abilityupped == "DEX":
                    DEX += 1
                elif abilityupped == "CON":
                    CON += 1
                elif abilityupped == "WIS":
                    WIS += 1
                elif abilityupped == "INT":
                    INT += 1
                elif abilityupped == "CHA":
                    CHA += 1
                break
            else:
                print("Please enter a valid ability")
    else:
        notZero = True
        while notZero is True:
            abilitydeducted = random.choice(abilities)
            if abilitydeducted == "STR":
                if STR != 0:
                    STR -= 1
                    notZero = False
            elif abilitydeducted == "DEX":
                if DEX != 0:
                    DEX -= 1
                    notZero = False
            elif abilitydeducted == "CON":
                if CON != 0:
                    CON -= 1
                    notZero = False
            elif abilitydeducted == "WIS":
                if WIS != 0:
                    WIS -= 1
                    notZero = False
            elif abilitydeducted == "INT":
                if INT != 0:
                    INT -= 1
                    notZero = False
            elif abilitydeducted == "CHA":
                if CHA != 0:
                    CHA -= 1
                    notZero = False
            print(f"Unfortunately, you lost. -1 will be deducted from a random ability. The ability chosen is: {abilitydeducted}")
    print("\nThank you for playing the Lucky Dice Game!")
    displayStats(playerName)
    canPlayLuckyDice = False
    return breakOption()

# Break Option Event

def breakOption():
    options = ["Continue with your adventure", "Try your dice luck", "Show Stats", "End Game"]
    print("\nBreak! Would you like to:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    try:
        choice = int(input("Enter your choice (1-4): "))
    except:
        print("Invalid choice! Please choose again.")
        return breakOption()
    if choice == 1:
        print("Okay, let's carry on with your adventure!")
        time.sleep(1)
    elif choice == 2:
        if canPlayLuckyDice is True:
            print("Okay, let's try your luck with dice!")
            print("\n\nWelcome to the Lucky Dice Game!\n\nIn this game, there will be 3 rounds to play, with 3 different die (d6, d20 and d100). In each round, you will roll a dice, and if it lands above or on the half of the dices value, +1 will be added to a random ability of yours! However, if the roll is less than half of the dice's value, -1 will be taken from a random ability of yours! High risk, high reward! You have the option to quit now if you would like, but once the game has started, there is no going back!")
            diceLuck()
        else:
            print("Sorry, you cannot play Lucky Dice again this break, try again next break!")
            return breakOption()
    elif choice == 3:
        displayStats(playerName)
        time.sleep(3)
        return breakOption()
    elif choice == 4:
        print("Alright, then this concludes your adventure! Thank you for playing Hydrovolter's Dungeons and Dragons Game! ")
        time.sleep(3)
        exit()
    else:
        print("Invalid choice! Please choose again.")
        return breakOption()

# First Event

def firstEvent(player_name, enemy_name, rating, xp_gain):
    print(f"\n\nWhile walking around, you encounter a {enemy_name}. It backs you into a corner. There is nowhere to run, you must fight the {enemy_name}. (Challenge Rating: {rating}/8) FIGHT STARTED:")
    time.sleep(3)
    player = Character(player_name, CON, STR, 3)
    enemy = Character(enemy_name, 5, 2, 1)

    player_actions = ActionPanel(player)
    enemy_actions = ActionPanel(enemy)
    battleLive = True
    while battleLive is True:
        time.sleep(1)
        option = battle_choice()
        if option == "attack":
            roll1 = d20()
            print(f"\nRoll 10 or higher to attack (D20). You rolled a... {roll1}!")
            time.sleep(1)
            if roll1 >= 10:
                attack = player_actions.attack(enemy)
                # enemy_actions.defend()
                if attack == "defeat":
                    # print(f"The Fight is Over! {player_name} wins!")
                    print(f"Congratulations on defeating your first enemy! From this fight, you have gained {str(xp_gain)} XP!")
                    add_xp(xp, xp_gain)
                    break
            else:
                attackmiss = ["You accidentally slipped and fell", "You missed your strike", "Your attack missed", "You tripped over a rock", "You hit your head on a bar", "Your strike just skimmed the enemy but didn't do any damage"]
                print(f"{random.choice(attackmiss)}. {enemy_name} takes this opportunity to strike!\n")
                time.sleep(1)
                attack2 = enemy_actions.attack(player)
                if attack2 == "defeat":
                    # print(f"The Fight is Over! {player_name} loses.")
                    print("Unfortunately, you have been defeated, which concludes your adventure. Thanks for playing!")
                    time.sleep(3)
                    exit()
                    # break

        elif option == "defend":
            player_actions.defend()
            time.sleep(1)
            attack3 = enemy_actions.attack(player)
            if attack3 == "defeat":
                # print(f"The Fight is Over! {player_name} loses.")
                print("Unfortunately, you have been defeated, which concludes your adventure. Thanks for playing!")
                time.sleep(3)
                exit()
                 # break
        elif option == "heal":
            player_actions.heal()
            time.sleep(1)

# Second Event

def secondEvent(xp_gain):
    global STR, DEX, CON, WIS, INT, CHA
    options = ["Take a Rest", "Scavenge Nearby"]
    itemsWizard = ["spellbook", "potion", "wand", "broomstick", "pot", "ingredients", "spellcaster", "cauldron"]
    itemsFighter = ["axe", "glaive", "longsword", "maul", "whip", "trident", "bow", "warhammer"]
    itemsMonk = ["spear", "shortsword", "club", "dagger", "handaxe", "javelin", "mace", "sickle"]
    print("\nWould you like to:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    try:
        choice = int(input("Enter your choice (1, or 2): "))
    except:
        print("Invalid choice! Please choose again.")
        return diceLuck()
    if choice == 1:
        print("You lay down for a bit, until your eyes slowly close. +2 CHA")
        CHA += 2
        time.sleep(1)
    elif choice == 2:
        if Class == "fighter": item = random.choice(itemsFighter)
        if Class == "wizard": item = random.choice(itemsWizard)
        if Class == "monk": item = random.choice(itemsMonk)

        print(f"You go scavenging, and find a {item}.")
        if item in itemsFighter:
            print("As you are in the fighter class, this grants you +1 DEX")
            DEX += 1
        elif item in itemsWizard:
            print("As you are in the wizard class, this grants you +1 STR")
            STR += 1
        elif item in itemsMonk:
            print("As you are in the monk class, this grants you +1 INT")
            INT += 1
    else:
        print("Invalid choice! Please choose again.")
        return secondEvent(random.randint(400, 800))
    time.sleep(2)
    print("\nOn a nearby wall, an inscription is marked. Do you see it, or not? Roll 10 or above on the D20 to discover it. You roll...")
    roll = d20()
    time.sleep(1)
    print(f"A {str(roll)}!\n")
    if roll >= 10:
        print("You spot the inscription and walk over to investigate further")
        if INT > 12:
            print("As your intelligence is above 12, you look closely and discover that there is a treasure map indicating some treasure beneath your feet!")
            if WIS > 10:
                print(f"As your wisdom is above 10, you realise there is a shovel nearby to dig up the ground, and you uncover the treasure! +1 to all ability stats! You are also rewarded with {str(xp_gain)} XP!")
                STR += 1
                DEX += 1
                CON += 1
                WIS += 1
                INT += 1
                CHA += 1
                add_xp(xp, xp_gain)
            else:
                print("However, as your wisdom is less than 10, you don't spot anything to dig up with, and give up.")
        else:
            print("As your intelligence is below 12, you are not able to decode the inscription")
    else:
        print("You don't see the inscription, and just continue walking.")

# Third Event TODO

def thirdEvent():
    pass


# Create Start Game Function

def startGame(player_name):
    global canPlayLuckyDice
    print(f"\nHello {player_name}, welcome to Hydrovolter's Dungeons and Dragons Python Game! Before we get started, you will need to create your character! Please proceed with the following: (5 Seconds)\n")
    time.sleep(5)
    # Setting + First Event
    createCharacter(player_name)
    createSetting()
    firstEvent(player_name, "FLUMPH", "1", random.randint(200, 400))
    # Break
    checkLevel()
    canPlayLuckyDice = True
    breakOption()
    # Second Event
    print("\n\nAfter fighting an intense battle, you find a post and lie against it.")
    secondEvent(random.randint(400, 800))
    # Break 2
    checkLevel()
    canPlayLuckyDice = True
    breakOption()
    # Third Event
    # thirdEvent()

def debug():
    pass



# Start Game

if __name__ == "__main__":
    playerNameInput = input("What is your name? ")
    playerName = playerNameInput.strip()
    if playerName == "": playerName = "Player"
    startGame(playerName)


# debug()
