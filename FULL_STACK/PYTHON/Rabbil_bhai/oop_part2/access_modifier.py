class father:
    x = 20
    y = 30

    def addTwo(self):
        print(self.x + self.y)

class son(father):
    pass

obj = son()
obj.addTwo()