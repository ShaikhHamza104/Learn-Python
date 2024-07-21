class Enimal:
    # say method is created 
    def say(self):
        print("Someting ")

class Dog(Enimal):
    # Override say method for base class
    def say(self):
        print("BOW BOW")

dog=Dog()
dog.say()