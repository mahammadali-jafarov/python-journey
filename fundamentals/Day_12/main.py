def swap_values(a,b):

    '''
    The Pythonic Swap: Write a function swap_values(a, b) 
    that takes two variables and swaps their values using tuple packing and unpacking in a single line. 
    Return the swapped values as a tuple.
    '''
    #CODE

    #short way
    #return b,a
    a,b=b,a
    tup=(a,b)   
    return tup 

def get_bookends(tup):

    '''
    Tuple Slicing & Indexing: Write a function get_bookends(tup) 
    that takes a tuple of any length (assume at least 3 elements). 
    Return a new tuple containing only the first, middle, and last elements of the original tuple. 
    (Hint: Use integer division // to find the middle index).
    '''
    #CODE
    mid_index=len(tup)//2
    new_tup=(tup[0],tup[mid_index],tup[-1])
    return new_tup

def analyze_numbers(lst):

    '''
    Multiple Returns: Write a function analyze_numbers(lst) 
    that takes a list of numbers. It should calculate the minimum, maximum, and 
    average of the list, and return all three values simultaneously as a tuple.
    '''
    #CODE

    #short way
    #return min(lst), max(lst), sum(lst) / len(lst)

    total=0
    for number in lst:
        total+=number
    average=total/len(lst)
    return min(lst),max(lst),average

def append_to_inner(tup,item):

    '''
    The Mutability Illusion: Write a function append_to_inner(tup, item). 
    You are given a tuple containing a list, for example: ([1, 2], "hello"). 
    Append the item to the inner list and return the tuple. 
    (This demonstrates that while a tuple cannot be changed, mutable items inside it can be!)
    '''
    #CODE
    for i in tup:
        if isinstance(i,list):
            i.append(item)
            break
    return tup

def sort_students(student_list):
    '''
    Sorting by Tuple Elements: Write a function sort_students(student_list) 
    that takes a list of tuples, where each tuple is (name, age, grade). 
    Sort the list primarily by grade (highest to lowest), and if there's a tie, 
    sort by name (alphabetically). (Hint: Use the key parameter in sorted() with a lambda function).
    '''
    #CODE

    #other way
    # Step 1: Sort by name alphabetically (A-Z)
    #by_name = sorted(student_list, key=lambda s: s[0])
    
    # Step 2: Sort by grade highest-to-lowest (ties preserve the A-Z name order!)
    #return sorted(by_name, key=lambda s: s[2], reverse=True)

    return sorted(student_list,key=lambda student: (-student[2],student[0]))


def build_grid(points):

    '''
    Coordinate Mapping (Tuples as Keys): Write a function build_grid(points). 
    Tuples are hashable, meaning they can be used as dictionary keys! 
    Given a list of tuples representing (x, y) coordinates, 
    return a dictionary where the keys are the coordinates and 
    the values are string labels: "Q1", "Q2", "Q3", or "Q4" based on which quadrant the coordinate falls into. 
    (Ignore zeroes for simplicity).
    '''
    #CODE
    quadrant_dict={}
    for coordinates in points:
        x,y=coordinates
        
        if x>0 and y>0:
            quadrant_dict[coordinates]="Q1"
        elif x<0 and y>0:
            quadrant_dict[coordinates]="Q2"
        elif x<0 and y<0:
            quadrant_dict[coordinates]="Q3"
        elif x>0 and y<0:
            quadrant_dict[coordinates]="Q4"
        else:
            quadrant_dict[coordinates]="the origin"

    return quadrant_dict
        
def custom_zip(list1,list2):

    '''
    Manual Zipping: Python has a built-in zip() function 
    that merges two lists into a list of tuples. Write your own function custom_zip(list1, list2) that does this manually. 
    Constraint: If the lists are different lengths, pad the shorter one with None so no data is lost. 
    (e.g., [1, 2] and ['a'] becomes [(1, 'a'), (2, None)]).
    '''
    #CODE
    max_len=max(len(list1),len(list2))
    new_list=[]
    
    for index in range(max_len):
        if index<len(list1):
            val1=list1[index]
        else:
            val1=None
        if index<len(list2):
            val2=list2[index]
        else:
            val2=None
        new_list.append((val1,val2))
    return new_list

if __name__ == "__main__":

    # Exercise 1: swap_values
    print("--- Exercise 1: Swap Values ---")
    print(swap_values(10, 99))  
    # Expected: (99, 10)

    # Exercise 2: get_bookends
    print("\n--- Exercise 2: Get Bookends ---")
    print(get_bookends(("A", "B", "C", "D", "E")))  
    # Expected: ('A', 'C', 'E')
    print(get_bookends((10, 20, 30, 40)))           
    # Expected: (10, 30, 40) (Because 4//2 is index 2)

    # Exercise 3: analyze_numbers
    print("\n--- Exercise 3: Analyze Numbers ---")
    print(analyze_numbers([2, 4, 6, 8, 10]))  
    # Expected: (2, 6.0, 10) -> (min, average, max)

    # Exercise 4: append_to_inner
    print("\n--- Exercise 4: Append to Inner ---")
    print(append_to_inner(([1, 2], "hello"), 3))  
    # Expected: ([1, 2, 3], 'hello')

    # Exercise 5: sort_students
    print("\n--- Exercise 5: Sort Students ---")
    students = [("Alice", 20, 85), ("Bob", 22, 95), ("Charlie", 19, 95)]
    print(sort_students(students))  
    # Expected: [('Bob', 22, 95), ('Charlie', 19, 95), ('Alice', 20, 85)]

    # Exercise 6: build_grid
    print("\n--- Exercise 6: Coordinate Mapping ---")
    points = [(5, 5), (-2, 3), (-4, -4), (6, -1), (0, 0)]
    print(build_grid(points))  
    # Expected: {(5, 5): 'Q1', (-2, 3): 'Q2', (-4, -4): 'Q3', (6, -1): 'Q4', (0, 0): 'the origin'}

    # Exercise 7: custom_zip
    print("\n--- Exercise 7: Manual Zipping ---")
    print(custom_zip([1, 2, 3], ['a', 'b']))  
    # Expected: [(1, 'a'), (2, 'b'), (3, None)]
    print(custom_zip([99], ['x', 'y', 'z']))  
    # Expected: [(99, 'x'), (None, 'y'), (None, 'z')]