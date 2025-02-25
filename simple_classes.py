
def main():
    d1 = Dog()
    d2 = Dog()
    d1.bark()
    d2.bark()
    Dog.bark(d2)

class Dog:
    def bark(self):  # 'this'
        print("woof! woof!")

# instance = Class()
main()