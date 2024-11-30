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
    pass

# SOn can access fathers method constructer
#Son().mulTwo()
#obj = Son()
#print(obj.x)
#obj.addTwo()

father().addTwo()
obj1 = father()
print(obj1.x)
obj1.addTwo()