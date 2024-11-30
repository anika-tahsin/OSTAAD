print("Welcome to Calculator Project")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

option = input("Enter your choice: ")

if option == '1':
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    sum = num1 + num2
    print("The result of the addition is = " + str(sum))

elif option == '2':
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    sub = num1 - num2
    print("The result of the substraction is = " + str(sub))

elif option == '3':
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    mul = num1 * num2
    print("The result of the Multiplication is = " + str(mul))

elif option == '4':
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    div = num1 / num2
    print("The result of the Division is = " + str(div))
else: 
    print("Choose from option 1 to 4.")
