class planet(object):
    color = ["blue","yellow","red","grey"]
    size = ["S","M", "L", "XL"]

    def __init__(self, size, color):
        self.sizeIndex = size
        seld.colorIndex = color

    def __str__(self):
        face = planet.size[self.sizeIndex]
        suit = planet.color[self.colorIndex]
        return size + color
