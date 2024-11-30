class father:
    __x = 20
    __y = 10
    def addTwo(self):
        print(self.__x + self.__y)

obj = father()
obj.addTwo()
print(obj.__x)