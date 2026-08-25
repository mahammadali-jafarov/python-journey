def classify_even_or_odd():
    """Classify an integer as even or odd with a ternary expression."""
    number = int(input("Enter a number: "))
    result = "Even" if number % 2 == 0 else "Odd"
    print(result)


def classify_number_sign():
    """Print whether an integer is positive, negative, or zero."""
    number = int(input("Enter any number: "))
    if number > 0:
        print("The number is positive")
    elif number < 0:
        print("The number is negative")
    else:
        print("The number is zero")


def classify_letter():
    """Classify an English letter as a vowel or consonant."""
    letter = input("Enter a letter from the English alphabet: ").upper()
    vowels = "AEIOU"
    consonants = "BDFGHJKLMNPQRSTVWXYZ"
    if letter in vowels:
        print("The letter is a vowel")
    elif letter in consonants:
        print("The letter is a consonant")
    else:
        print("Please enter a letter only!")


def find_maximum_of_two():
    """Find the larger of two integers without using max()."""
    first_number = int(input("Enter a number: "))
    second_number = int(input("Enter a number: "))
    if first_number > second_number:
        print("The first number is larger: ", first_number)
    elif first_number < second_number:
        print("The second number is larger: ", second_number)
    else:
        print("The numbers are equal")


def check_exam_result():
    """Print whether an exam score is passing."""
    score = int(input("Enter your score: "))
    result = (
        "Congratulations, you passed!"
        if score >= 51
        else "Unfortunately, you failed"
    )
    print(result)


def fizz_buzz():
    """Print Fizz, Buzz, FizzBuzz, or the number according to divisibility."""
    number = int(input("Enter a number: "))
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)


def calculate_bmi():
    """Calculate and classify body mass index."""
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print("Underweight", bmi)
    elif 18.5 <= bmi < 25:
        print("Normal weight", bmi)
    elif 25 <= bmi < 30:
        print("Overweight", bmi)
    else:
        print("Obesity", bmi)


def classify_triangle():
    """Classify a triangle by the equality of its side lengths."""
    first_side = int(input("Enter the first side: "))
    second_side = int(input("Enter the second side: "))
    third_side = int(input("Enter the third side: "))
    if first_side == second_side == third_side:
        print("The triangle is equilateral")
    elif (
        first_side == second_side
        or second_side == third_side
        or first_side == third_side
    ):
        print("The triangle is isosceles")
    else:
        print("The triangle is scalene")


def find_quadrant():
    """Determine the quadrant or axis containing a point."""
    x_coordinate = float(input("Enter x: "))
    y_coordinate = float(input("Enter y: "))
    if x_coordinate > 0 and y_coordinate > 0:
        print("Quadrant I")
    elif x_coordinate < 0 and y_coordinate > 0:
        print("Quadrant II")
    elif x_coordinate < 0 and y_coordinate < 0:
        print("Quadrant III")
    elif x_coordinate > 0 and y_coordinate < 0:
        print("Quadrant IV")
    elif x_coordinate == 0 and y_coordinate == 0:
        print("The point is at the origin (0, 0)")
    elif x_coordinate == 0:
        print("The point is on the y-axis")
    else:
        print("The point is on the x-axis")


def play_rock_paper_scissors():
    """Determine the winner of a two-player rock-paper-scissors game."""
    print("Rock-Paper-Scissors Game")
    first_player = input("Player 1: Rock, Paper, or Scissors?: ").lower()
    second_player = input("Player 2: Rock, Paper, or Scissors?: ").lower()
    choices = ["rock", "paper", "scissors"]
    if first_player not in choices or second_player not in choices:
        print("Please enter one of the three choices in the correct format")
    elif first_player == second_player:
        print("Tie")
    elif (
        (first_player == "paper" and second_player == "rock")
        or (first_player == "rock" and second_player == "scissors")
        or (first_player == "scissors" and second_player == "paper")
    ):
        print("Player 1 gets 1 point")
    else:
        print("Player 2 gets 1 point")


def check_leap_year_nested():
    """Check a leap year using nested conditionals."""
    year = int(input("Enter a year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year")
            else:
                print("Not a leap year")
        else:
            print("Leap year")
    else:
        print("Not a leap year")


def find_maximum_of_three():
    """Find the largest of three integers with nested if-else blocks."""
    print("Enter three different numbers.")
    first_number = int(input())
    second_number = int(input())
    third_number = int(input())
    if first_number > second_number:
        if first_number > third_number:
            print(first_number)
        else:
            print(third_number)
    else:
        if second_number > third_number:
            print(second_number)
        else:
            print(third_number)


def simulate_atm():
    """Simulate PIN verification, balance lookup, and withdrawal."""
    correct_pin = "1234"
    balance = 500
    pin = input("Enter your PIN: ")
    if pin == correct_pin:
        print("Which operation would you like to perform?")
        print("1. Check balance", "2. Withdraw money")
        choice = int(input("Enter the operation number (1 or 2): "))
        if choice == 2:
            amount = int(input("Enter the amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Remaining balance: ", balance)
            else:
                print("Insufficient funds")
        elif choice == 1:
            print("Balance: ", balance)
    else:
        print("Incorrect PIN!")


if __name__ == "__main__":
    '''
    here you can see what is returned by calling each function separately (uncomment)
    '''
    # classify_even_or_odd()
    # classify_number_sign()
    # classify_letter()
    # find_maximum_of_two()
    # check_exam_result()
    # fizz_buzz()
    # calculate_bmi()
    # classify_triangle()
    # find_quadrant()
    # play_rock_paper_scissors()
    # check_leap_year_nested()
    # find_maximum_of_three()
    # simulate_atm()
    pass
