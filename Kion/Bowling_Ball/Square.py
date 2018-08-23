from random import randint
class Square:
    def __init__(self, length, a, c, d):
        self.length = length
a = randint(1, 50)
print("Your side length is " + str(a) + " inches for your square")
c = a * a
print("Your area is " + str(c) + "inches for your square")
d = 4 * a
print("Your perimeter is " + str(d) + "inches for your square")
class Rectangle(Square):
    def length(self, x, y, g, h):
        x = randint(1, 50)
        y = randint(1, 50)
        return x, y
print("Your width is " + str(x) + "inches for your rectangle")
y = randint(1, 50)
print("Your length is " + str(y) + "inches for your rectangle")
g = x + y + x + y
h = x * y
print("Your area is " + str(h) + "inches for your rectangle")
print("Your perimeter is " + str(g) + "inches for your rectangle")