"""
li = [1,2,3]
li.reverse()
print(li)
"""

"""
x = 6
print(dir(x))
"""
"""
# class variable, instance variable
class MyClass:
    value1 = 10 

a_obj = MyClass()
print(type(a_obj))
print(a_obj.value1)

a_obj.value1 = 20 

b_obj = MyClass()
print(type(a_obj))
print(a_obj.value1)
"""
class Car:
    color = "White"

car1 = Car()
car2 = Car()
car3 = Car()

car1.color = "Red"

print(car1.color, car2.color, car3.color)