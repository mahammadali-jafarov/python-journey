
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
    return "She said, \"Python's escape characters are easy!\"\n"

def format_profile(name,age,city):
    
    '''
      Formatting: Write a function format_profile(name, age, city) 
      that takes three variables and uses an f-string to return: 
      "Profile: [name] is [age] years old and lives in [city]."
    '''
    #ode
    return f"Profile: {name} is {age} years old and lives in {city}."

def clean_strings(s):

    '''
    Modify Methods: Write a function clean_string(s) that takes a string, 
    converts it entirely to lowercase, 
    removes any leading or trailing whitespace,
    and replaces all remaining spaces with underscores (_).
    '''
    #code
    l=s.lower().strip().replace(" ", "_")
    return l

def count_word(word,text):

    '''
    Search Methods: Write a function count_word(word, text) that returns how many times the word appears in the text, 
    ignoring case differences (e.g., "code", "Code", and "CODE" all count).

    '''
    #code
    count = text.lower().count(word.lower())
    return  f"word '{word}' count: {count}"
def is_palindrome(s):

    '''
    Slicing & Modifying: Write a function is_palindrome(s) that checks if a string reads the same forwards and backwards. 
    Constraint: ignore spaces and case differences, and use string slicing ([::-1]) to determine the result.
    '''
    #code
    cleaned_s=s.lower().replace(" ","")
    return cleaned_sed==cleaned_s[::-1]
  
    

def format_list(s):
    '''
    Formatting & Methods: Write a function format_list(s) that takes a messy, 
    comma-separated string like " john , MARY , pEter " and returns a clean,
    numbered list string separated by newlines:
        1. John
        2. Mary
        3. Peter
    '''
    #code
    string_list=s.title().split(",")
    for i in string_list:
        string_list
    



if __name__ == "__main__":
    #first_and_last("String Slicing")
    #print(print_quote())
    #print(format_profile("Mahammadali",20,"Baku"))
    #clean_strings("Strings Methods")
    #print(count_word("code","Writing cOdE is fun. I like to write CoDe "))
    print(is_palindrome("Tenet"))
    #format_list(" john , Mary , pEter ")
    


