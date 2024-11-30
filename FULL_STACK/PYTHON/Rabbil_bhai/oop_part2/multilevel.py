class grandfather():
    x = 10
    y = 20
    def addTwo(self):
        print(self.x + self.y)

class father(grandfather):
    pass

class son(father):
    pass


class grandSon(son):
    pass

objgrandson = grandSon()
objgrandson.addTwo()
