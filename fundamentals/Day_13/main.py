import string

def count_unique_chars(string):

    '''
    The Deduplicator: Write a function count_unique_chars(string) 
    that returns the exact number of unique characters in a given string, 
    ignoring spaces and capitalization. (e.g., "Hello World" -> 7).
    '''
    #CODE
    return len(set(string.lower().replace(" ","")))

def is_allowed(allowed_ips,target_ip):

    '''
    Fast Membership: Write a function is_allowed(allowed_ips, target_ip). 
    allowed_ips is a list of thousands of IP addresses.
    First, convert it to a set for speed, then check if target_ip is in it. Return True or False.
    '''
    #CODE
    set_of_ip=set(allowed_ips)
    return target_ip in set_of_ip

def find_common_elements(list1,list2,list3):

    '''
    Three-Way Intersection: Write a function find_common_elements(list1, list2, list3). 
    Convert them to sets and use set intersection methods to return a list of elements 
    that appear in all three lists.
    '''
    #CODE
    common_set=set(list1) & set(list2) & set(list3)
    return list(common_set)
    
def exclusive_students(class_a,class_b):
    
    '''
    Symmetric Difference: Write a function exclusive_students(class_a, class_b). 
    Given two lists of student names, use set operations to return a set of students 
    who are taking Class A OR Class B, but not both.
    '''
    #CODE
    return set(class_a) ^ set(class_b)

def is_pangram(sentence):

    '''
    The Pangram Checker: Write a function is_pangram(sentence). 
    A pangram is a sentence containing every letter of the alphabet at least once 
    (like "The quick brown fox jumps over the lazy dog"). Use sets to verify this efficiently. Return True or False
    '''
    #CODE
    sentence_set=set(sentence.lower())
    alphabet_set=set(string.ascii_lowercase)

    # Does the sentence set contain all the letters of the alphabet set?
    return sentence_set.issuperset(alphabet_set)


if __name__ == "__main__":

    # Exercise 8: count_unique_chars
    print("--- Exercise 8: The Deduplicator ---")
    print(count_unique_chars("Hello World"))  
    # Expected: 7 (unique characters: 'h', 'e', 'l', 'o', 'w', 'r', 'd')

    # Exercise 9: is_allowed
    print("\n--- Exercise 9: Fast Membership ---")
    allowed = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]
    print(is_allowed(allowed, "10.0.0.1"))    # Expected: True
    print(is_allowed(allowed, "192.168.1.50")) # Expected: False

    # Exercise 10: find_common_elements
    print("\n--- Exercise 10: Three-Way Intersection ---")
    l1 = [1, 2, 3, 4, 5]
    l2 = [3, 4, 5, 6, 7]
    l3 = [5, 4, 9, 10, 3]
    print(find_common_elements(l1, l2, l3))  
    # Expected: [3, 4, 5] (or {3, 4, 5})

    # Exercise 11: exclusive_students
    print("\n--- Exercise 11: Symmetric Difference ---")
    class_a = ["Alice", "Bob", "Charlie"]
    class_b = ["Bob", "David", "Charlie"]
    print(exclusive_students(class_a, class_b))  
    # Expected: {'Alice', 'David'}

    # Exercise 12: is_pangram
    print("\n--- Exercise 12: The Pangram Checker ---")
    print(is_pangram("The quick brown fox jumps over the lazy dog")) # Expected: True
    print(is_pangram("Hello World"))                                # Expected: False