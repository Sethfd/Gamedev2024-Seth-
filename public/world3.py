import random

class Room:
    def __init__(self, description):
        self.description = description
        self.enemies = []
        self.items = []

    def add_enemy(self, enemy):
        self.enemies.append(enemy)

    def add_item(self, item):
        self.items.append(item)

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def is_alive(self):
        return self.health > 0

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10

    def is_alive(self):
        return self.health > 0

def battle(player, enemy):
    while player.is_alive() and enemy.is_alive():
        print(f"You attack {enemy.name} for {player.attack} damage.")
        enemy.health -= player.attack
        print(f"{enemy.name} has {enemy.health} health left.")

        if enemy.is_alive():
            print(f"{enemy.name} attacks you for {enemy.attack} damage.")
            player.health -= enemy.attack
            print(f"You have {player.health} health left.")
        
        if not player.is_alive():
            print("You have been defeated!")
            break

def main():
    # Create rooms
    room1 = Room("You are in a dimly lit room.")
    room2 = Room("You enter a damp and musty chamber.")
    
    # Create enemies
    goblin = Enemy("Goblin", 30, 5)
    orc = Enemy("Orc", 50, 8)

    # Add enemies to rooms
    room1.add_enemy(goblin)
    room2.add_enemy(orc)

    # Initialize player
    player_name = input("Enter your character's name: ")
    player = Player(player_name)

    # Game loop
    current_room = room1
    while player.is_alive():
        print(current_room.description)
        
        if current_room.enemies:
            for enemy in current_room.enemies:
                if enemy.is_alive():
                    print(f"A wild {enemy.name} appears!")
                    battle(player, enemy)
                    if not player.is_alive():
                        break
            current_room.enemies = [enemy for enemy in current_room.enemies if enemy.is_alive()]

        # Move to the next room
        next_room = input("Do you want to go to the next room? (yes/no) ")
        if next_room.lower() == 'yes':
            current_room = room2  # For simplicity, always move to room2
        else:
            print("You decided to stay in the room.")
    
    print("Game over.")

if __name__ == "__main__":
    main()
