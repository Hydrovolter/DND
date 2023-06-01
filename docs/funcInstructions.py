# XP System Usage:

# xp = add_xp(xp, 1000)
# print("Player is now level", get_level(xp)) # Output: Player is now level 3

# ActionPanel System Usage:

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

"""
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
"""