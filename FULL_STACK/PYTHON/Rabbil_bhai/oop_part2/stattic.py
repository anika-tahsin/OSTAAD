class Profile:
    x = 20
    y = 30

    @staticmethod
    def addTwo():
        z = Profile.x+ Profile.y
        print(z)

Profile.addTwo()