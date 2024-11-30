class father:
    x = 20
    y = 30

    def __init__(self):
        z = self.x - self.y
        print(z)
    
    def addTwo(self):
        z = self.x+ self.y
        print(z)

    @staticmethod
    def mulTwo():
        z = father.x * father.y
        print(z)

class Son(father):
    x = 10
    y = 5
    
    def addTwo(self):
        z = self.x+ self.y
        print(z)

# If we use overrided properties from son
objSon = Son()
objSon.addTwo()