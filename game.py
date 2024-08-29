# This is the main class for any character in the game
class Character:
    # This sets up the character's name, starting health, and empty inventory
    def __init__(self, name):
        self.name = name 
        self.health = 100    # Every character starts with 100 health points
        self.inventory = []  # The inventory starts empty

    # This describes the character, showing their name, health, and what items they have
    def describe(self):
        print(f"Character: {self.name}")
        print(f"Health: {self.health}")
        print(f"Inventory: {self.inventory}")

    # This reduces the character's health when they get hurt
    def take_damage(self, amount):
        self.health -= amount  # Decrease health by the damage amount
        if self.health < 0:  # Make sure health doesn’t go below 0
            self.health = 0
        print(f"{self.name} took {amount} damage and now has {self.health} health.")

    # This adds  add an item to the character's inventory
    def pick_item(self, item):
        self.inventory.append(item)  # Add the item to the inventory
        print(f"{self.name} picked up: {item}")

# Encapsulation: The Character class puts everything about a character (name, health, items)
# and what they can do (like describe themselves, take damage, pick up items) in one place.

# Inheritance: The Hero class gets everything from the Character class (like name, health, and actions)
# without needing to write the same code again.
class Hero(Character):
    # This method lets the hero heal by adding more health
    def heal(self, amount):
        self.health += amount  # Increase the hero's health by the given amount

# Inheritance: The Villain class gets everything from the Character class, like name, health, and actions, without needing to write that code again.
class Villain(Character):
    # Polymorphism: Overriding the describe method to give a more evil description.
    def describe(self):
        print(f"{self.name} is a fearsome villain with {self.health} health and the following evil items: {self.inventory}")

# Abstraction: The Adventure class provides a simple interface to manage scenes
# and character interactions, hiding the complex details.
class Adventure:
    # This sets up an adventure with empty lists for characters and scenes
    def __init__(self):
        self.characters = []  # List to hold characters in the adventure
        self.scenes = {}  # Dictionary to hold scene names and descriptions

    # This method adds a new scene with a name and description
    def add_scene(self, name, description):
        self.scenes[name] = description  # Store the scene with its description

    # This method shows a specific scene in the adventure base on its name
    def play_scene(self, name):
        if name in self.scenes:  # Check if the scene exists
            print(f"Scene: {name}")
            print(self.scenes[name])  # Show the scene's description
            self.character_action()  # Call a method for chatacters to act
        else:
            print(f"Scene '{name}' not found in this adventure.")  # Handle missing scenes

      # This is a placeholder for what characters can do in a scene
    def character_action(self):
        print("Character takes an action...")  # Example of what could happen 

# Example of how the classes work together

# Creates a Hero object named "Archer"
archer = Hero(name="Archer")

# Creates a Villain object named "Goblin"
goblin = Villain(name="Goblin")

# Creates an Adventure object
adventure = Adventure()

# Add scenes to the adventure
adventure.add_scene("Forest", "You are in a dark forest. There's a shiny object on the ground.")
adventure.add_scene("Cave", "The cave is dark and you can hear growling.")

# Plays the "Forest" scene
adventure.play_scene("Forest")
print(f"{archer.name} looks around and sees the shiny object.")

# Hero picks up an item (Shiny Sword)
archer.pick_item("Shiny Sword")

# Describes the hero to show their current state
archer.describe()

# Plays the "Cave" scene
adventure.play_scene("Cave")
print(f"{archer.name} cautiously enters the cave, ready for anything.")

# Hero takes damage (loses 20 health points)
archer.take_damage(20)

# Describes the hero again to see the updated state
archer.describe()