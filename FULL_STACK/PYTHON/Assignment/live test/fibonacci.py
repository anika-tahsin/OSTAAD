    
def fibonacci_num_generator(number):
    if number <= 0:
        return []
    elif number == 1:
        return [0]
    elif number == 2:
        return [0,1]
        
    fibonacci_series = [0,1]
    for index in range(2, number):
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_term)
    return fibonacci_series
    
        
def fibonacci_max_num_generator(max_value):
    if max_value < 0:
        return []
    fibonacci_series = [0,1]
    while True:
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        if next_term > max_value:
            break
        fibonacci_series.append(next_term)
    return fibonacci_series
    
def input_validation(input_number):
    try:
        value = int(input_number)
        if value < 0:
            raise ValueError
        return value
    except ValueError:
        print("Please enter a positive number")
        return None


while True:
    print("Welcome to  Fibonacci series generator")
    print("1. Generate Fibonacci series by number of terms")
    print("2. Generate Fibonacci series by maximum value")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Generating Fibonacci series by number of terms")
        while True:
            number = input("Enter the number of terms: ")
            number = input_validation(number)
            if number is not None:
                break
        
        fib_series = fibonacci_num_generator(number)
        print(f"\nFibonacci series {number} terms: ")
        print(", ".join(map(str, fib_series)))

    elif choice == "2":
        print("Generating Fibonacci series by by maximum value")
        while True:
            max_value = input("Enter the maximum value: ")
            max_value = input_validation(max_value)
            if max_value is not None:
                break
        
        fib_series = fibonacci_max_num_generator(max_value)
        print(f"\nFibonacci series {max_value} terms: ")
        print(", ".join(map(str, fib_series)))

    elif choice == "3":
        print("Thank you")
            