colors = ["pink", "blue", "red", "black"]
person = "Ferd", "Berfel"
name = "Joe Smith"
values = {'a':10, 'm': 99, 'f': 8}
things = {5, 9, 8, 4}
# -------------
rcolors = reversed(colors)
ecolors = enumerate(colors)

with open('DATA/mary.txt') as mary_in:
    line = next(mary_in)  # consume next element of iterator
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print()
print(f"{colors = }")
icolors = iter(colors) # get the list iterator for the list
x = next(icolors)
print(f"{x = }")
print(f"{next(icolors) = }")
print(f"{next(icolors) = }")
print(f"{next(icolors) = }")
# print(f"{next(icolors) = }")
print()

for color in colors:
    print(color)