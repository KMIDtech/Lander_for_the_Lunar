class MyPet:
    def __init__ (self, name):
        self.name = name
    def bark(self):
        print("Your pet " + self.name + " has been barking. Go care for it!")
Fat_Cat = MyPet("Bongo")
Cute_Puppy = MyPet("Caeser Salad")
Fat_Cat.bark()
class MyLizard(MyPet):
    def eat_flies(self):
        print("Your lizard " + self.name + " has been eating flies.")
Lizard = MyLizard("Godzilla")
Lizard.eat_flies()
Lizard.bark()