#Build a Zoo management system with classes for animals, cages, and zoo operations.
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def feed(self):
        print(f"{self.name} has been fed.")
    def __str__(self):

        return f"{self.name} the {self.species} ({self.age} years old)"

class Cage:
    def __init__(self, cage_id, cage_type):
        self.cage_id = cage_id
        self.cage_type = cage_type
        self.animals =[]

    def add_animal(self, animal):
        if len(self.animals) < 5:
            self.animals.append(animal)
            print(f"{animal.name} has been added to Cage {self.cage_id}.")
        else:
            print(f"Cannot add {animal.name}. Cage {self.cage_id} is full!")

    def remove_animal(self, animal_name):
        for animal in self.animals:
            if animal.name == animal_name:
                self.animals.remove(animal)
                print(f"{animal_name} has been removed from Cage {self.cage_id}.")
                return
            print(f"No animal named {animal_name} found in Cage {self.cage_id}.")

    def list_animals(self):
        if not self.animals:
            print(f"Cage {self.cage_id} is empty.")
        else:
            print(f"Animals in Cage {self.cage_id}:")
            for animal in self.animals:
                print(animal)

    def get_cage_id(self):
        return self.cage_id

    def __str__(self):
        return f"Cage {self.cage_id} ({self.cage_type}): {len(self.animals)} animals"

class Zoo:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.cages = []

    def add_cage(self, cage):
        self.cages.append(cage)
        print(f"Cage {cage.get_cage_id()} added to Zoo {self.name}.")

    def remove_cage(self, cage_id):
        for cage in self.cages:
            if cage.get_cage_id() == cage_id:
                self.cages.remove(cage)
                print(f"Cage {cage_id} removed from Zoo {self.name}.")
                return
            print(f"Cage {cage_id} not found.")

    def find_animal(self, animal_name):
        for cage in self.cages:
            for animal in cage.animals:
                if animal.name == animal_name:
                    print(f"Animal {animal_name} found in Cage {cage.get_cage_id()}.")
                    print(animal)
                    return
        print(f"Animal {animal_name} not found in Zoo {self.name}.")

    def display_all_animals(self):
        print(f"\n--- List of Animals in Zoo {self.name} ---")
        for cage in self.cages:
            cage.list_animals()

    def feed_all_animals(self):
        for cage in self.cages:
            for animal in cage.animals:
                animal.feed()
if __name__ == "__main__":
    zoo = Zoo("Happy Zoo", "City Park")

    cage1 = Cage(1, "Carnivore Cage")
    cage2 = Cage(2, "Herbivore Cage")

    zoo.add_cage(cage1)
    zoo.add_cage(cage2)

    tiger = Animal("Tiger", "Panthera tigris", 5)
    parrot = Animal("Parrot", "Psittaciformes", 2)
    elephant = Animal("Elephant", "Elephas maximus", 10)

    cage1.add_animal(tiger)
    cage1.add_animal(parrot)
    cage2.add_animal(elephant)

    zoo.display_all_animals()
    print("\nFeeding all animals:")

    zoo.feed_all_animals()
    print("\nSearching for Tiger:")

    zoo.find_animal("Tiger")
    print("\nRemoving Parrot from Cage 1:")

    cage1.remove_animal("Parrot")

    zoo.display_all_animals()