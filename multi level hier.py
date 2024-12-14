class animal:
    def eat(self):
        print("animal is eating")

class mamal(animal):
    def walk(self):
        print("animal is walking")
class dog(mamal):
    def bark(self):
        print("dog is barking")

dog=dog()
dog.eat()
dog.walk()
dog.bark()
