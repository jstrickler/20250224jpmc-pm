class Dog:
    def __init__(self, breed, name):
        self._breed = breed
        self._name = name
    
    @property
    def breed(self):
        return self._breed
    
    @property
    def name(self):
        return self._name

d1 = Dog("Mutt", "Andy")
d2 = Dog("English Shepherd", "Nellie")

print(f"{d1.name = }")
print(f"{d1.breed = }")

attr_name = "breed"
print(f"{getattr(d1, attr_name) = }")

d1_attributes = [attr for attr in dir(d1) if not attr.startswith('_')]
print(f"{d1_attributes = }")
for attribute_name in d1_attributes:
    attribute_value = getattr(d1, attribute_name)
    print(attribute_name, attribute_value, type(attribute_value))

setattr(Dog, "bark", lambda self: print("woof! woof!"))

d1.bark()
d2.bark()

# getattr(x, "name")  == x.name