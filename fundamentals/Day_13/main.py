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
    return target_ip in list(set_of_ip)

        

def find_common_elements(list1,list2,list3):

    '''
    Three-Way Intersection: Write a function find_common_elements(list1, list2, list3). 
    Convert them to sets and use set intersection methods to return a list of elements 
    that appear in all three lists.
    '''
    #CODE
    
    
def exclusive_strudents(class_a,class_b):
    
    '''
    Symmetric Difference: Write a function exclusive_students(class_a, class_b). 
    Given two lists of student names, use set operations to return a set of students 
    who are taking Class A OR Class B, but not both.
    '''
    #CODE

def is_pangram(sentence):

    '''
    The Pangram Checker: Write a function is_pangram(sentence). 
    A pangram is a sentence containing every letter of the alphabet at least once 
    (like "The quick brown fox jumps over the lazy dog"). Use sets to verify this efficiently. Return True or False
    '''
    #CODE

def find_pair_values(lst,target):

    '''
    Fast Two-Sum (O(n) time): Write a function find_pair_values(lst, target). 
    Instead of finding indices, find the actual two numbers that add up to the target. 
    Constraint: You must use a single for loop and a set to track numbers you've already seen. 
    Return the pair as a tuple, or None if no pair exists.
    '''
    #CODE

def longest_consecutive(nums):

    '''
    Longest Consecutive Sequence: Write a function longest_consecutive(nums). 
    Given an unsorted list of integers, find the length of the longest consecutive elements sequence.
    Example: [100, 4, 200, 1, 3, 2] -> The longest consecutive sequence is [1, 2, 3, 4], so return 4.
    Algorithmic trick: Convert the list to a set. Then, only start counting a sequence 
    if the number is the start of a sequence (i.e., num - 1 is not in the set).
    This allows you to solve a complex sorting problem in O(n) time!
    '''
    #CODE


if __name__=="__main__":

    print(count_unique_chars("Hello World"))