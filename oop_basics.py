# Part 4.1: Basic Class Structure
class PartyAnimal:
    def __init__(self, name: str) -> None:
        self.name = name
        self.count = 0
        print(f"{self.name} constructed")
    
    def party(self) -> None:
        self.count += 1
        print(f"{self.name} party count: {self.count}")

# Part 4.2 & 4.3: Inheritance and Type Hinting
class Hero:
    """Represents a generic hero character."""
    def __init__(self, name: str, health: int) -> None:
        self.name: str = name
        self.health: int = health
        print(f"{self.name} joined the game!")

    def attack(self) -> None:
        print(f"{self.name} performed a basic attack!")

class Warrior(Hero):
    """Represents a specialized Warrior class inheriting from Hero."""
    def __init__(self, name: str, health: int, weapon: str) -> None:
        super().__init__(name, health)
        self.weapon: str = weapon

    def special_move(self) -> None:
        print(f"{self.name} used their {self.weapon} for a special move!")

# Testing the implementation
if __name__ == "__main__":
    s = PartyAnimal("Sally")
    s.party()

    warrior = Warrior(name="Aragorn", health=100, weapon="Sword")
    warrior.attack()
    warrior.special_move()
