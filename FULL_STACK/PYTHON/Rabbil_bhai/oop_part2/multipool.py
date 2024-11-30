class father:
    def addTwo(self, num1, num2):
        print(num1+num2)

class mother:
    def mulTwo(self, num1, num2):
        print(num1*num2)    

class Son(father,mother):
    pass


objSon = Son()
objSon.addTwo(1, 2)
objSon.mulTwo(3, 4)