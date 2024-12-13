def generate_fibonacci_terms(n):
    """Generate a Fibonacci series containing exactly 'n' terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fibonacci_series = [0, 1]
    for i in range(2, n):
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_term)
    return fibonacci_series


def generate_fibonacci_max_value(max_value):
    """Generate all Fibonacci numbers less than or equal to 'max_value'."""
    if max_value < 0:
        return []
    
    fibonacci_series = [0, 1]
    while True:
        next_term = fibonacci_series[-1] + fibonacci_series[-2]
        if next_term > max_value:
            break
        fibonacci_series.append(next_term)
    return fibonacci_series


def validate_input(input_value):
    """Validate that the user input is a non-negative integer."""
    try:
        value = int(input_value)
        if value < 0:
            raise ValueError
        return value
    except ValueError:
        print("Invalid input! Please enter a non-negative integer.")
        return None


def main():
    print("Welcome to the Fibonacci Series Generator!")
    
    # Ask user for the number of terms
    while True:
        num_terms = input("Enter the number of terms you want in the Fibonacci series: ")
        num_terms = validate_input(num_terms)
        if num_terms is not None:
            break
    
    # Generate and display the series with 'num_terms'
    fib_terms = generate_fibonacci_terms(num_terms)
    print(f"\nFibonacci series with {num_terms} terms:")
    print(", ".join(map(str, fib_terms)))
    
    # Ask user for the maximum value
    while True:
        max_value = input("\nEnter the maximum value for the Fibonacci series: ")
        max_value = validate_input(max_value)
        if max_value is not None:
            break
    
    # Generate and display all Fibonacci numbers less than or equal to 'max_value'
    fib_max_value = generate_fibonacci_max_value(max_value)
    print(f"\nFibonacci numbers less than or equal to {max_value}:")
    print(", ".join(map(str, fib_max_value)))


# Run the program
if __name__ == "__main__":
    main()
