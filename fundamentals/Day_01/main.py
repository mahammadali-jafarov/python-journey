def convert_currency():
    """Convert an AZN amount to USD using the rate 1 USD = 1.70 AZN."""
    amount = float(input("Enter the amount in AZN: "))
    amount = amount / 1.70
    print(round(amount,2), "USD")


def show_square_and_cube():
    """Print the square and cube of an integer."""
    number = int(input("Enter a number: "))
    square = number ** 2
    cube = number ** 3
    print("The square of the number: ", square)
    print("The cube of the number: ", cube)


def check_even_or_odd():
    """Print boolean results indicating whether an integer is odd or even."""
    number = int(input("Enter a number: "))
    odd_marker, even_marker = 1, 0
    remainder = number % 2
    print("The number is odd: ", odd_marker is remainder)
    print("The number is even: ", even_marker is remainder)


def calculate_circle_area():
    """Calculate a circle's area using pi = 3.14."""
    radius = float(input("Enter the circle's radius: "))
    area = 3.14 * (radius ** 2)
    print(area)


def swap_values():
    """Swap and print two user-provided values."""
    first_value = input("Enter the value of a: ")
    second_value = input("Enter the value of b: ")
    first_value, second_value = second_value, first_value
    print("a:", first_value, "b:", second_value)


def convert_seconds():
    """Convert total seconds into hours, minutes, and seconds."""
    total_seconds = int(input("Enter the total number of seconds: "))
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    print("Hours:", hours, "Minutes:", minutes, "Seconds:", seconds)


def sum_three_digit_number():
    """Sum the digits of a three-digit integer using arithmetic operators."""
    number = int(input("Enter a three-digit number: "))
    last_digit = number % 10
    middle_digit = (number // 10) % 10
    first_digit = number // 100
    digit_sum = first_digit + middle_digit + last_digit
    print(digit_sum)


def calculate_distance():
    """Calculate the distance between two points."""
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print(distance)


def calculate_compound_interest():
    """Calculate the final amount for compound interest."""
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate: "))
    years = float(input("Enter the number of years: "))
    amount = principal * ((1 + (rate / 100)) ** years)
    print("Final amount: ", round(amount, 2))


def check_range():
    """Check whether a number is between two inclusive integer limits."""
    lower_limit = int(input("Enter the lower limit: "))
    upper_limit = int(input("Enter the upper limit: "))
    number = int(input("Enter the number to check: "))
    print(lower_limit <= number and upper_limit >= number)


def reverse_four_digit_number():
    """Reverse a four-digit integer using arithmetic operators."""
    number = int(input("Enter a four-digit integer: "))
    reversed_number = (
        (number % 10) * 1000
        + ((number % 100) // 10) * 100
        + ((number // 100) % 10) * 10
        + number // 1000
    )
    print(reversed_number)


def check_triangle_inequality():
    """Check whether three side lengths can form a triangle."""
    first_side = float(input("Enter the first side: "))
    second_side = float(input("Enter the second side: "))
    third_side = float(input("Enter the third side: "))
    print(
        first_side + second_side > third_side
        and first_side + third_side > second_side
        and second_side + third_side > first_side
    )


def check_leap_year():
    """Check whether a year is a leap year."""
    year = int(input("Enter a year: "))
    print((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)


if __name__ == "__main__":
    convert_currency()
    # show_square_and_cube()
    # check_even_or_odd()
    # calculate_circle_area()
    # swap_values()
    # convert_seconds()
    # sum_three_digit_number()
    # calculate_distance()
    # calculate_compound_interest()
    # check_range()
    # reverse_four_digit_number()
    # check_triangle_inequality()
    # check_leap_year()
    
