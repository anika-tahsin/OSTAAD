"""
temp = 5
def func():

      temp = 10
      print(temp)

func()
print(temp)
"""
"""
li = [2,3]
li2 = [4,5]

li.extend(li2)

print(li)
"""

numbers = [5, 6, 7, 8, 9, 10]
print(numbers[5 : : 7])

li = [7, 15, 17, 9]
li[1:3] = [14, 48, 9]
print(li)

def calculate():
    a = 20 
    b= 1.0  
    sum = a+ b
    min = a-b
    print(sum,min)

calculate()