from abc import ABC,abstractmethod

class father(ABC):
    x = 20
    y = 30

    @abstractmethod
    def addTwo(self):
        z = self.x+ self.y
        print(z)

class Son(father):
    def addTwo(self):
        z = self.x+ self.y
        print(z)

#fatherobj = father()
#fatherobj.addTwo()

sonobj = Son()
sonobj.addTwo()