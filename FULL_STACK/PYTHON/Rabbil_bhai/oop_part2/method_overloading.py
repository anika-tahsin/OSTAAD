class father:
    def addNumbers(self, a,b,c=0):
        print(a+b+c)

    def myNumbers(self, *args):
        print(*args)

obj = father()
obj.addNumbers(2,3,4)
obj.addNumbers(2,3)

obj.myNumbers(2,3,4,5)
