import random

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
    match choice:
        case 1:
            return "attack"
        case 2:
            return "defend"
        case 3:
            return "heal"
        case _:
            print("Invalid choice! Please choose again.")
            return battle_choice()
 
if __name__ == "__main__":
    pass
