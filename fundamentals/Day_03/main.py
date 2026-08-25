def sum_numbers_to_n():
    """Calculate the sum of all integers from 1 through N."""
    number = int(input("Enter a positive integer: "))
    total = 0
    for value in range(1, number + 1):
        total += value
    print("Sum of the numbers from 1 to", number, ":", total)


def print_multiplication_table():
    """Print the multiplication table for a number from 1 through 10."""
    number = int(input("Enter a number: "))
    for value in range(1, 11):
        result = number * value
        print(f"{number} x {value} = {result}")


def print_even_numbers():
    """Print even numbers from 1 through 20 using continue."""
    for value in range(1, 21):
        if value % 2 != 0:
            continue
        else:
            print(value)


def request_password_until_correct():
    """Request a password until the correct password is entered."""
    while True:
        password = input("Enter the password: ")
        if password == "python123":
            print("Login successful")
            break


def sum_digits_with_while():
    """Calculate a positive integer's digit sum arithmetically."""
    number = int(input("Enter a positive integer: "))
    total = 0
    while number > 0:
        digit = number % 10
        total += digit
        number = number // 10
    print(total)


def check_prime_number():
    """Check whether a number is prime using a for-else loop."""
    number = int(input("Enter a positive number: "))
    if number <= 1:
        print("The number is neither prime nor composite (or it is negative)")
    else:
        for divisor in range(2, number):
            if number % divisor == 0:
                print("The number is composite")
                break
        else:
            print("The number is prime")


def calculate_factorial():
    """Calculate N factorial with a loop."""
    number = int(input("Enter a number: "))
    factorial = 1
    for value in range(1, number + 1):
        factorial *= value
    print(f"Factorial: {factorial}")


def print_fibonacci_sequence():
    """Print the first N terms of the Fibonacci sequence."""
    number = int(input("Enter a number: "))
    first, second = 0, 1
    while number > 0:
        print(first, end=" ")
        first, second = second, first + second
        number -= 1


def reverse_integer_with_while():
    """Reverse an integer arithmetically with a while loop."""
    number = int(input("Enter an integer of any length: "))
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = (reversed_number * 10) + digit
        number //= 10
    print("Reversed number: ", reversed_number)


def demonstrate_pass_and_break():
    """Skip multiples of five and stop at 23 while printing other values."""
    for value in range(1, 31):
        if value % 5 == 0:
            pass
        elif value == 23:
            break
        else:
            print(value)


def print_star_pyramid():
    """Print a centered star pyramid of the requested height."""
    height = int(input("Enter the pyramid height: "))
    for row in range(1, height + 1):
        for _ in range(height - row):
            print(" ", end="")
        for _ in range(2 * row - 1):
            print("*", end="")
        print()


def find_perfect_numbers():

    """Calculate proper-divisor sums for numbers from 1 through 1000."""
    
    for number in range(1, 1001):
        divisor_sum = 0
        for divisor in range(1, number):
            if number % divisor == 0:
                divisor_sum = divisor_sum + divisor
        if divisor_sum==number:
            print(number)


if __name__ == "__main__":

    '''
    here you can run what is returned by calling each function separately (uncomment).
    '''
    # sum_numbers_to_n()
    # print_multiplication_table()
    # print_even_numbers()
    # request_password_until_correct()
    # sum_digits_with_while()
    # check_prime_number()
    # calculate_factorial()
    # print_fibonacci_sequence()
    # reverse_integer_with_while()
    # demonstrate_pass_and_break()
    # print_star_pyramid()
    #find_perfect_numbers()
    pass
