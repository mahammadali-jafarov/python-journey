def character_count(word):

    '''
    Frequency Counter: Write a function character_count(word) 
    that takes a string and returns a dictionary where the keys are the characters and 
    the values are how many times they appear. (e.g., "aba" -> {'a': 2, 'b': 1}).
    '''
    #CODE
    character_count_dict={}
    for char in word: 
        character_count_dict[char]=word.count(char)
    return character_count_dict

def generate_squares(n):

    '''
    Dictionary Comprehension: Write a function generate_squares(n) 
    that uses a single dictionary comprehension to return a dictionary 
    where the keys are numbers from 1 to n, and the values are their squares. (e.g., n=3 -> {1: 1, 2: 4, 3: 9}).
    '''
    #CODE
    return {i:i**2 for i in range(1,n+1)}

def invert_dict(d):
    '''
    Inverting: Write a function invert_dict(d) that swaps the keys and values. 
    Assume all values in the original dictionary are unique. (e.g., {'a': 1} becomes {1: 'a'}).
    '''
    #CODE
    inverted_dict={}
    for key,value in d.items():
        inverted_dict[value]=key
    return inverted_dict

def filter_passing_grades(grade_dict):
        
    '''
    Filtering: Write a function filter_passing_grades(grade_dict). 
    Return a new dictionary containing only the students (keys) whose grades (values) are 70 or higher.
    '''
    #CODE
    higher_grades={}
    for key,value in grade_dict.items():
        if value>=70:
            higher_grades[key]=value
    return higher_grades

def merge_inventories(inv1,inv2):

    '''
    Merging with Logic: Write a function merge_inventories(inv1, inv2). 
    Merge both dictionaries into a new one. If a key exists in both, add their values together in the new dictionary.
    '''
    #CODE
    merge_inv=inv1.copy()
    for key,value in inv2.items():
        merge_inv[key]=merge_inv.get(key,0) + value
    return merge_inv


if __name__ =="__main__":

    #Exercise 1
    print(character_count("ababaacc"))  #Expected: {'a':4, 'b':2, 'c':2}

    #Exercise 2
    print(generate_squares(3))    #Expected: {1: 1, 2: 4, 3:9}

    #Exercise 3
    print(invert_dict({'a':1}))  #Expected: {1:'a'}

    #Exercise 4
    print(filter_passing_grades({'Michael': 85, 'Juliette': 65, 'Hannah': 75})) # Expected: {'Michael': 85, 'Hannah': 75}

    #Exercise 5
    print(merge_inventories({"apples": 5, "bananas": 2}, {"apples": 3, "oranges": 4})) # Expected: {'apples': 8, 'bananas': 2, 'oranges': 4}