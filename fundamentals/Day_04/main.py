def eucliean_algorithm():

    '''GCD (Greatest Common Divisor) and LCM (Least Common Multiple) calculation  with while loop '''

    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    default_first_number ,default_second_number = first_number,second_number 

    while second_number>0:
        first_number,second_number=second_number, first_number % second_number

    gcd=first_number
    lcm=(default_first_number*default_second_number)//gcd
    print("GCD (Greatest Common Divisor): ",gcd)
    print("LCD (Least Common Multiple): ",lcm)


if __name__ == "main":
    eucliean_algorithm()
