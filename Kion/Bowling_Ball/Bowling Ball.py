print("You, by some  miraculous means, have acquired an amazing bowling ball. How far do you want it to go?(Take notice that gravity will be inacted and the distance you want it to go will be minimized!!!!)")

z = input()
class BowlingBall:
    def __init__ (self, x, y):
        self.radius = x
        self.weight = y
    def rolling (self, z):
        distance = z
        total = z - self.weight
        return total

x = 39
y = 9
var_namme = BowlingBall(x,y)
total = var_namme.rolling(z)
print("Your ball's weight will be" + str(var_namme.weight) + "pounds and its radius will be" + str(var_namme.radius) + "inches.")
print("The ball will be rolling" + str(total) + "yards")