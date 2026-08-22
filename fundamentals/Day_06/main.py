
def first_and_last(s):

    '''
    Slicing: Write a function first_and_last(s) that takes a string s.
    If the string is less than 6 characters long, return "Too short". 
    Otherwise, use slicing to return a new string made of the first 3 and the last 3 characters concatenated together
    
    ''' 
    #code
    if len(s)<6:
        return "Too short" 
    return s[:3]+s[-3:]

def print_quote():

    '''
      Concatenation & Escape Characters: 
      Create a function print_quote() that returns exactly this string, 
      including the quotation marks and the newline character at the end:
      She said, "Python's escape characters are easy!"\n
    
    '''
    #code
    return "She said, \"Pyhton's escape characters are easy!\"\n"

def format_profile(name,age,city):
    
    '''
      Formatting: Write a function format_profile(name, age, city) 
      that takes three variables and uses an f-string to return: 
      "Profile: [name] is [age] years old and lives in [city]."
    '''
    #ode
    return f"Profile: {name} is {age} years old and lives in {city}."

