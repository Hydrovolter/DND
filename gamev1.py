# Made by Hydrovolter#8432
#
#
# Import Modules

import random
import time
import sys
import os
from colorama import Fore # If Colorama module isn't installed/supported, switch colours with terminal ASCII

# Import Functions (Modules)

from funcs.actionpanel import *
from funcs.dicerolls import *
from funcs.xpsystem import *
from funcs.asciiart import *

cls = lambda: os.system('cls' if os.name=='nt' else 'clear')

def opening():
    cls()
    print("Made by " + Fore.GREEN + "Hydrovolter" + Fore.BLACK)

    time.sleep(1) # Carriage Return
    print("\r.", end="")
    time.sleep(1)
    print("\r..", end="")
    time.sleep(1)
    print("\r...\n\n", end="")
    time.sleep(1)

    start_ascii()
    time.sleep(2)

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
setting = None
patron = ""


# Create Character

def createCharacter(character_name):
    global STR, DEX, CON, WIS, INT, CHA
    # global race
    # global Class
    # global xp

    # Abilities
    print(Fore.CYAN + "\nAbilities:\n\n" + Fore.BLUE + "Strength (STR)\nDexterity (DEX)\nConstitution (CON)\nWisdom (WIS)\nIntelligence (INT)\nCharisma (CHA)\n" + Fore.CYAN)
    abilities = ["STR", "DEX", "CON", "WIS", "INT", "CHA"]
    scores = [15, 14, 13, 12, 10, 8]

    for _, score in enumerate(scores):
        ability = None
        while ability not in abilities:
            num = score
            ability = input(Fore.CYAN + f"Choose an ability to be score {num} (Use shortened version): " + Fore.WHITE)
            ability = ability.upper()

            if ability in abilities:
                if globals()[ability] == 0:
                    globals()[ability] = num
                    break
                else:
                    print(Fore.RED + "You cannot choose an ability you have already chosen!")
                    ability = None
            else:
                print(Fore.RED + "Please enter a valid ability")

    time.sleep(1)

    print(Fore.CYAN + "\nAbility Stats:\n")
    print(Fore.CYAN + "Name: " + Fore.BLUE + character_name)
    print(Fore.CYAN + "Strength: " + Fore.BLUE + str(STR))
    print(Fore.CYAN + "Dexterity: " + Fore.BLUE + str(DEX))
    print(Fore.CYAN + "Constitution: " + Fore.BLUE + str(CON))
    print(Fore.CYAN + "Wisdom: " + Fore.BLUE + str(WIS))
    print(Fore.CYAN + "Intelligence: " + Fore.BLUE + str(INT))
    print(Fore.CYAN + "Charisma: " + Fore.BLUE + str(CHA))

    time.sleep(3)

    # Race
    races = ["human", "elf", "dwarf", "half-orc", "tiefling", "half-elf", "dragonborn", "gnome", "halfling"] # added from dwarf [3]
    print(Fore.CYAN + "\nRaces:")
    racePrint = ""
    for raceName in races:
        racePrint = racePrint + "\n" + raceName.capitalize()
    print(Fore.BLUE + racePrint + "\n" + Fore.CYAN)

    global race
    race = None
    while race not in races:
        race = input(Fore.CYAN + "Choose a race: " + Fore.WHITE)
        racelowered = race.lower()
        if racelowered in races:
            race = racelowered
            match racelowered:
                case "human":
                    STR += 1
                    DEX += 1
                    CON += 1
                    WIS += 1
                    INT += 1
                    CHA += 1
                case "elf":
                    DEX += 2
                    WIS += 2
                case "dwarf":
                    STR += 1
                    CON += 2
                case "half-orc": # added from here
                    STR += 2
                    CON += 1
                case "tiefling":
                    INT += 1
                    CHA += 2
                case "half-elf":
                    INT += 1
                    CHA += 2
                case "dragonborn":
                    STR += 2
                    CHA += 1
                case "gnome":
                    INT += 2
                    DEX += 1
                case "halfling":
                    DEX += 2
                    CON += 1
            break
        else:
            print(Fore.RED + "Please enter a valid race")

    time.sleep(1)

    print(Fore.CYAN + "\nUpdated Ability Stats:\n")
    print(Fore.CYAN + "Name: " + Fore.BLUE + character_name)
    print(Fore.CYAN + "Strength: " + Fore.BLUE + str(STR))
    print(Fore.CYAN + "Dexterity: " + Fore.BLUE + str(DEX))
    print(Fore.CYAN + "Constitution: " + Fore.BLUE + str(CON))
    print(Fore.CYAN + "Wisdom: " + Fore.BLUE + str(WIS))
    print(Fore.CYAN + "Intelligence: " + Fore.BLUE + str(INT))
    print(Fore.CYAN + "Charisma: " + Fore.BLUE + str(CHA))
    print(Fore.CYAN + "Race: " + Fore.BLUE + race.capitalize())

    time.sleep(3)

    # Class
    classes = ["fighter", "wizard", "monk"]
    print(Fore.CYAN + "\nClasses:")
    classPrint = ""
    for className in classes:
        classPrint = classPrint + "\n" + className.capitalize()
    print(Fore.BLUE + classPrint + Fore.CYAN)
    global Class
    Class = None
    while Class not in classes:
        Class = input(Fore.CYAN + "\nChoose a class: " + Fore.WHITE)
        classlowered = Class.lower()
        if classlowered in classes:
            if classlowered == "fighter":
                print(Fore.BLUE + "Fighters are profecient with weapons, and are natural leaders, with good constitution. +2 STR, +2 CHA, and +1 CON. However, they aren't the smartest of creatures. -2 INT, -1 WIS")
                Class = "fighter"
                STR += 2
                CHA += 2
                CON += 1
                INT -= 2
                WIS -= 1
            elif classlowered == "wizard":
                print(Fore.BLUE + "Wizards are quite smart, being able to memorise and perform a variety of spells. +2 INT, +2 WIS, +1 DEX. However, they aren't natural leaders or have combat prowess. -2 CHA, -1 STR")
                Class = "wizard"
                INT += 2
                WIS += 2
                DEX += 1
                CHA -= 2
                STR -= 1
            elif classlowered == "monk":
                print(Fore.BLUE + "Monks are agile and fast, specialising in unarmed combat, so their body can naturally take more of a 'punch'. +2 DEX, +2 CON, +1 STR. However, they struggle in social aspects of life. -2 WIS, -1 INT ")
                Class = "monk"
                DEX += 2
                CON += 2
                STR += 1
                WIS -= 2
                INT -= 1
            break
        else:
            print(Fore.RED + "Please enter a valid race")

    time.sleep(3)

    print(Fore.CYAN + "\nUpdated Ability Stats:\n")
    print(Fore.CYAN + "Name: " + Fore.BLUE + character_name)
    print(Fore.CYAN + "Strength: " + Fore.BLUE + str(STR))
    print(Fore.CYAN + "Dexterity: " + Fore.BLUE + str(DEX))
    print(Fore.CYAN + "Constitution: " + Fore.BLUE + str(CON))
    print(Fore.CYAN + "Wisdom: " + Fore.BLUE + str(WIS))
    print(Fore.CYAN + "Intelligence: " + Fore.BLUE + str(INT))
    print(Fore.CYAN + "Charisma: " + Fore.BLUE + str(CHA))
    print(Fore.CYAN + "Race: " + Fore.BLUE + race.capitalize())
    print(Fore.CYAN + "Class: " + Fore.BLUE + Class.capitalize())

    time.sleep(3)

# Create Setting

def createSetting():
    global setting
    settingRoll = d4()
    setting = settingRoll
    print(Fore.BLUE + "\nRolling the D4 dice to choose the setting for this adventure...")
    time.sleep(3)
    print("You rolled a... " + Fore.WHITE + str(settingRoll) + Fore.BLUE + "!\n")
    time.sleep(1)
    if settingRoll == 1:
        # Stormy night in a lonely pub with drunk people
        print("In a stormy village, an isolated cozy pub offers refuge from the raging weather, its warmth and cheer a stark contrast to the thunder outside.")
    elif settingRoll == 2:
        # Countryside cozy house
        print("As the sun sets, a cozy house glows warmly with soft lights, crackling logs, and comfy furnishings, inviting you to linger and enjoy the peaceful evening.")
    elif settingRoll == 3:
        # Swamp/Forest
        print("In the heart of a lush, swampy forest, a tree house, woven into the trees with vines and leaves, offers a retreat with misty views and the rhythmic creaking of its wooden structure.")
    elif settingRoll == 4:
        # Urban Jungle (City)
        print("In the midst of a city's chaos, a tall skyscraper reflects the urban buzz, providing views of the bustling streets and the constant hum of traffic, embodying the city's relentless energy.")
    time.sleep(5)

# Check Level

def checkLevel():
    global STR, DEX, INT, CON, lastLevel

    # lastLevel = get_level(xp)
    if get_level(xp) > lastLevel:
        print(Fore.GREEN + "Congratulations! " + Fore.BLUE + "You levelled up! Your current level is: " + Fore.WHITE + {str(get_level(xp))})
        time.sleep(2)
        print(Fore.BLUE + "Levelling up grants you benefits depending on your class! You have a 1/2 chance of gaining +1 CON or +1 STR, INT, or DEX.")
        time.sleep(2)
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
    print(Fore.CYAN + "\nUpdated Ability Stats:\n")
    print(Fore.CYAN + "Name: " + Fore.BLUE + character_name)
    print(Fore.CYAN + "Strength: " + Fore.BLUE + str(STR))
    print(Fore.CYAN + "Dexterity: " + Fore.BLUE + str(DEX))
    print(Fore.CYAN + "Constitution: " + Fore.BLUE + str(CON))
    print(Fore.CYAN + "Wisdom: " + Fore.BLUE + str(WIS))
    print(Fore.CYAN + "Intelligence: " + Fore.BLUE + str(INT))
    print(Fore.CYAN + "Charisma: " + Fore.BLUE + str(CHA))
    print(Fore.CYAN + "Race: " + Fore.BLUE + race.capitalize())
    print(Fore.CYAN + "Class: " + Fore.BLUE + Class.capitalize())

# Dice Luck Game

def diceLuck():
    options = ["Play the Lucky Dice game", "Exit the Lucky Dice Game"]
    print(Fore.BLUE + "\nWould you like to:")
    for i, option in enumerate(options):
        print(Fore.CYAN + f"{i+1}. " + Fore.BLUE + f"{option}")
    try:
        choice = int(input(Fore.CYAN + "Enter your choice (1, or 2): " + Fore.WHITE))
    except:
        print(Fore.RED + "Invalid choice! Please choose again.")
        return diceLuck()
    if choice == 1:
        print(Fore.GREEN + "Okay, let's play!")
        time.sleep(2)
        playDiceLuck()

    elif choice == 2:
        print(Fore.BLUE + "Okay, returning to break menu!")
        breakOption()
    else:
        print(Fore.RED + "Invalid choice! Please choose again.")
        return diceLuck()

def playDiceLuck():
    global STR, DEX, CON, WIS, INT, CHA, canPlayLuckyDice
    abilities = ["STR", "DEX", "CON", "WIS", "INT", "CHA"]

    # Round 1

    r1 = d6()
    print(Fore.BLUE + "Round 1: You roll a...")
    time.sleep(3)
    print(Fore.WHITE + f"{str(r1)}!")
    time.sleep(1)
    if r1 >= 3:
        print(Fore.GREEN + "Congratulations! You won!")

        ability = None
        while ability not in abilities:
            ability = input(Fore.CYAN + "Please pick an ability to add +1 to! (STR, DEX, CON, WIS, INT, CHA): ")
            abilityupped = ability.upper()
            if abilityupped in abilities:
                match abilityupped:
                    case "STR":
                        STR += 1
                    case "DEX":
                        DEX += 1
                    case "CON":
                        CON += 1
                    case "WIS":
                        WIS += 1
                    case "INT":
                        INT += 1
                    case "CHA":
                        CHA += 1
                break
            else:
                print(Fore.RED + "Please enter a valid ability")
    else:
        notZero = True
        while notZero is True:
            abilitydeducted = random.choice(abilities)
            match abilitydeducted:
                case "STR":
                    if STR != 0:
                        STR -= 1
                        notZero = False
                case "DEX":
                    if DEX != 0:
                        DEX -= 1
                        notZero = False
                case "CON":
                    if CON != 0:
                        CON -= 1
                        notZero = False
                case "WIS":
                    if WIS != 0:
                        WIS -= 1
                        notZero = False
                case "INT":
                    if INT != 0:
                        INT -= 1
                        notZero = False
                case "CHA":
                    if CHA != 0:
                        CHA -= 1
                        notZero = False
            print(Fore.BLUE + "Unfortunately, you lost. -1 will be deducted from a random ability. The ability chosen is: " + Fore.WHITE + abilitydeducted)

        # Round 2
    time.sleep(3)
    r2 = d20()
    print(Fore.BLUE + "Round 2: You roll a...")
    time.sleep(3)
    print(Fore.WHITE + f"{str(r2)}!")
    time.sleep(1)
    if r2 >= 10:
        print(Fore.GREEN + "Congratulations! You won!")

        ability = None
        while ability not in abilities:
            ability = input(Fore.CYAN + "Please pick an ability to add +1 to! (STR, DEX, CON, WIS, INT, CHA): ")
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
                print(Fore.RED + "Please enter a valid ability")
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
            print(Fore.BLUE + "Unfortunately, you lost. -1 will be deducted from a random ability. The ability chosen is: " + Fore.WHITE + abilitydeducted)

    # Round 3
    time.sleep(3)
    r3 = d100()
    print(Fore.BLUE + "Round 3 (Final Round): You roll a...")
    time.sleep(3)
    print(Fore.WHITE + f"{str(r3)}!")
    time.sleep(1)
    if r3 >= 50:
        print(Fore.GREEN + "Congratulations! You won!")

        ability = None
        while ability not in abilities:
            ability = input(Fore.CYAN + "Please pick an ability to add +1 to! (STR, DEX, CON, WIS, INT, CHA): ")
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
                print(Fore.RED + "Please enter a valid ability")
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
            print(Fore.BLUE + "Unfortunately, you lost. -1 will be deducted from a random ability. The ability chosen is: " + Fore.WHITE + abilitydeducted)
    time.sleep(3)
    print(Fore.GREEN + "\nThank you for playing the Lucky Dice Game!")
    time.sleep(2)
    displayStats(playerName)
    canPlayLuckyDice = False
    return breakOption()

# Break Option Event

def breakOption():
    options = ["Continue with your adventure", "Try your dice luck", "Show Stats", "Clear Screen (CLS)", "End Game"]
    print(Fore.BLUE + "\nBreak! Would you like to:")
    for i, option in enumerate(options):
        print(Fore.CYAN + f"{i+1}. " + Fore.WHITE + f"{option}")
    try:
        choice = int(input(Fore.CYAN + "Enter your choice (1-5): " + Fore.WHITE))
    except:
        print(Fore.RED + "Invalid choice! Please choose again.")
        return breakOption()
    if choice == 1:
        print(Fore.GREEN + "Okay, let's carry on with your adventure!")
        time.sleep(1)
    elif choice == 2:
        if canPlayLuckyDice is True:
            print(Fore.GREEN + "Okay, let's try your luck with dice!")
            time.sleep(1)
            print(Fore.BLUE + "\n\nWelcome to the Lucky Dice Game!\n\n")
            time.sleep(1)
            print(Fore.BLUE + "In this game, there will be 3 rounds to play, with 3 different die (d6, d20 and d100).")
            time.sleep(1)
            print(Fore.BLUE + "In each round, you will roll a dice, and if it lands above or on the half of the dices value, +1 will be added to a random ability of yours!")
            time.sleep(1.75)
            print(Fore.BLUE + "However, if the roll is less than half of the dice's value, -1 will be taken from a random ability of yours! High risk, high reward!")
            time.sleep(1.75)
            print(Fore.BLUE + "You have the option to quit now if you would like, but once the game has started, there is no going back!")
            time.sleep(1.5)
            diceLuck()
        else:
            print(Fore.RED + "Sorry, you cannot play Lucky Dice again this break, try again next break!")
            return breakOption()
    elif choice == 3:
        displayStats(playerName)
        time.sleep(3)
        return breakOption()
    elif choice == 4:
        print(Fore.RED + "Clearing Screen for more space (CLS)... (3 seconds)")
        time.sleep(3)
        cls()
        return breakOption()
    elif choice == 5:
        print(Fore.RED + "Alright, then this concludes your adventure! Thank you for playing " + Fore.GREEN + "Hydrovolter's" + Fore.RED + " Dungeons and Dragons Game! ")
        time.sleep(3)
        sys.exit()
    else:
        print(Fore.RED + "Invalid choice! Please choose again.")
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
                    sys.exit()
                    # break

        elif option == "defend":
            player_actions.defend()
            time.sleep(1)
            attack3 = enemy_actions.attack(player)
            if attack3 == "defeat":
                # print(f"The Fight is Over! {player_name} loses.")
                print("Unfortunately, you have been defeated, which concludes your adventure. Thanks for playing!")
                time.sleep(3)
                sys.exit()
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

# Third Event

def thirdEvent(patron_name, player_name, enemy_name, rating, xp_gain, patron_rating):
    options = ["Accept", "Decline"]
    print("\nWould you like to:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    try:
        choice = int(input("Enter your choice (1, or 2): "))
    except:
        print("Invalid choice! Please choose again.")
        return diceLuck()
    if choice == 1:
        print(f"\nYou look for the {enemy_name}. Roll 40 or above on the D100 to discover it (Your wisdom score will be added to your final roll). You roll...")
        roll = d100()
        finalRoll = roll + WIS
        time.sleep(1)
        print(f"A {str(roll)} + {str(WIS)} = {str(finalRoll)}!\n")
        if finalRoll >= 40: # Fight FLUMPH
            print(f"\n\nAfter searching, you encounter the {enemy_name} (again). It backs you into a corner (again). There is nowhere to run (again). You must fight the {enemy_name} (agai- okay I'm getting deja-vu). (Challenge Rating: {rating}/8) FIGHT STARTED:")
            time.sleep(3)
            player = Character(player_name, CON, STR, 3)
            enemy = Character(enemy_name, 10, 4, 2)

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
                            print(f"Congratulations on defeating the {enemy_name}! From this fight, you have gained {str(xp_gain)} XP!")
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
                            sys.exit()
                            # break

                elif option == "defend":
                    player_actions.defend()
                    time.sleep(1)
                    attack3 = enemy_actions.attack(player)
                    if attack3 == "defeat":
                        # print(f"The Fight is Over! {player_name} loses.")
                        print("Unfortunately, you have been defeated, which concludes your adventure. Thanks for playing!")
                        time.sleep(3)
                        sys.exit()
                        # break
                elif option == "heal":
                    player_actions.heal()
                    time.sleep(1)
        else:
            print(f"You failed to find the {enemy_name}. You return to the {patron_name}")
    elif choice == 2: # Fight Patron
        print(f"Due to you declining his offer, a fight breaks out between you and the {patron_name}. (Challenge Rating: {patron_rating}/8) FIGHT STARTED:")
        time.sleep(3)
        player = Character(player_name, CON, STR, 3)
        enemy = Character(enemy_name, 12, 6, 3)

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
                        print(f"Congratulations on defeating the {patron_name}! From this fight, you have gained {str(xp_gain)} XP!")
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
                        sys.exit()
                        # break

            elif option == "defend":
                player_actions.defend()
                time.sleep(1)
                attack3 = enemy_actions.attack(player)
                if attack3 == "defeat":
                    # print(f"The Fight is Over! {player_name} loses.")
                    print("Unfortunately, you have been defeated, which concludes your adventure. Thanks for playing!")
                    time.sleep(3)
                    sys.exit()
                    # break
            elif option == "heal":
                player_actions.heal()
                time.sleep(1)
    else:
        print("Invalid choice! Please choose again.")
        return thirdEvent(patron, playerName, "Battle FLUMPH", "2", random.randint(400, 800), "3")


# Create Start Game Function

def startGame(player_name):
    global canPlayLuckyDice, patron
    print(Fore.RED + "\nHello " + Fore.BLUE + player_name + Fore.RED + ", welcome to Hydrovolter's Dungeons and Dragons Python Game! Before we get started, you will need to create your character! Please proceed with the following: (5 Seconds)\n")
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
    print(Fore.BLUE + "\n\nAfter fighting an intense battle, you find a post and lie against it.")
    secondEvent(random.randint(400, 800))

    # Break 2
    checkLevel()
    canPlayLuckyDice = True
    breakOption()

    # Third Event
    if setting == 1: patron = "Kenku"
    elif setting == 2: patron = "Goblin"
    elif setting == 3: patron = "Yuan-ti"
    elif setting == 4: patron = "Construct"
    print(f"A {patron} walks up to you and says: '{player_name}, you must defeat the evil FLUMPH before it is too late. It has recovered its strength and is now more powerful than before.")
    thirdEvent(patron, playerName, "Battle FLUMPH", "2", random.randint(400, 800), "3")

    # Break 3
    checkLevel()
    canPlayLuckyDice = True
    breakOption()


def debug():
    firstEvent("debug", "FLUMPH", "1", random.randint(200, 400))



# Start Game

if __name__ == "__main__":
    opening()

    playerNameInput = input(Fore.BLUE + "What is your name? " + Fore.WHITE)
    playerName = playerNameInput.strip()
    if playerName == "": playerName = "Player"

    startGame(playerName)

    #debug() # Debug Purposes (DEV Env)
