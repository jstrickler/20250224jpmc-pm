
class Animal:
    def move(self):
        print("moving...")

class Dog(Animal):
    def bark(self):
        print("woof! woof!")

d = Dog()
d.move()
d.bark()

class_name = "Cat"
class_method_name = "meow"
class_method = lambda self: print("meow meow")

Cat = type(class_name, (Animal,), {class_method_name: class_method})

c = Cat()
c.move()
c.meow()
