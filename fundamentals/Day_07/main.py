def rotate_left(s,k):

    '''
    Algorithmic Slicing (Rotation): Write a function rotate_left(s, k)
    that takes a string s and an integer k. It should return the string rotated left by k characters using slicing. 
    For example, rotate_left("Python", 2) should return "thonPy".

    '''
    #CODE
    return s[k:len(s)]+s[:k]

def replace_vowels(s):

    '''
    Algorithmic Modification: Write a function replace_vowels(s)
    that iterates through a string and returns a new string 
    where every vowel (a, e, i, o, u) is replaced by its index position in the string.
    '''
    #CODE
    result=""
    for i,char in enumerate(s):
        if char.lower() in "aeiou":
            result+=str(i)
        else:
            result+=char
    return result
    
def build_filepath(folder,filename):

    '''
    Escape Characters & Concatenation: Write a function build_filepath(folder, filename) 
    that safely concatenates a Windows folder path and a filename, 
    ensuring there is exactly one backslash '\' between them.

    Hint: Pay attention to how Python handles backslashes in strings.
    '''
    #CODE
    return "\\"+folder+"\\"+filename

def is_anagram(s1,s2):

    '''
    Algorithmic Modification (Anagrams): Write a function is_anagram(s1, s2) 
    that checks if two strings are anagrams of each other (contain the exact same characters in the exact same quantities). 
    Constraint: You may NOT use Python's built-in sort() function or the collections.Counter module. Rely on string methods like .count()
    '''
    #CODE
    first_string=s1.lower().replace(" ","")
    second_string=s2.lower().replace(" ","")
    if len(first_string)==len(second_string):
        return False

    for char in first_string:
        if first_string.count(char)!=second_string.count(char):
                return False
    return True



        
if __name__ == "__main__":
    #print(rotate_left("Python",2))
    #print(replace_vowels("Coding is fun"))
    #print(build_filepath("python_journey","main.py"))
    #print(is_anagram("Funeral","Real fun"))

    pass