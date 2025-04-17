class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        """Reduces hunger by 3 points (but not below 0) and increases happiness by 1."""
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)
        print(f"{self.name} is eating...")

    def sleep(self):
        """Increases energy by 5 points (but not above 10)."""
        self.energy = min(10, self.energy + 5)
        print(f"{self.name} is sleeping...")

    def play(self):
        """Decreases energy by 2, increases happiness by 2, and increases hunger by 1."""
        if self.energy >= 2:
            self.energy = max(0, self.energy - 2)
            self.happiness = min(10, self.happiness + 2)
            self.hunger = min(10, self.hunger + 1)
            print(f"{self.name} is playing...")
        else:
            print(f"{self.name} is too tired to play.")

    def get_status(self):
        """Prints the current state of the pet."""
        print(f"{self.name}'s current status: ")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Happiness: {self.happiness}")
        print(f"Tricks: {self.tricks}")

    def train(self, trick):
        """Teaches the pet a new trick and stores it in a list."""
        self.tricks.append(trick)
        print(f"{self.name} learned a new trick: {trick}!")

    def show_tricks(self):
        """Prints all learned tricks."""
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
