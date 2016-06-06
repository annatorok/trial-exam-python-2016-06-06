# Create a class that represents a cuboid:
# It should take it's three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume

class Cuboid():

    def __init__(self, length, width, heigth):
        self.length = length
        self.width = width
        self.heigth = heigth

    def getSurface(self):
        surface = 2*(self.length*self.width + 2*self.length*self.heigth + 2*self.width*self.heigth)
        return surface

    def getVolume(self):
        volume = self.length * self.width * self.heigth
        return volume

cuboidFirst = Cuboid(3,5,6)
print(cuboidFirst.getSurface())
print(cuboidFirst.getVolume())
