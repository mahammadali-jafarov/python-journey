def remove_duplicates(lst):

    '''
    Algorithmic Modification: Write a function remove_duplicates(lst) 
    that takes a list and returns a new list with all duplicates removed. 
    Constraint: You must maintain the original order of the first occurrences, and you may NOT use the set() function.
    '''

    #CODE

    unique_list=[]
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def chunk_list(lst,size):

    '''
    Looping & Aggregation (Chunking): Write a function chunk_list(lst, size) 
    that breaks a flat list into a list of lists (chunks), where each sub-list contains exactly size elements. 
    If the last chunk has fewer elements, that is acceptable. For example, chunk_list([1,2,3,4,5], 2) returns [[1,2], [3,4], [5]].
    '''

    #CODE

    return [lst[i:i+size] for i in range(0,len(lst),size)]

def sort_by_length(words):

    '''
    Sorting with Logic: Write a function sort_by_length(words) 
    that takes a list of strings and sorts them based on the length of each string, 
    from shortest to longest. Constraint: Use the key parameter of the sort() method or sorted() function.
    '''

    return sorted(words, key=len)

def move_zeroes(lst):

    '''
    List Methods (In-Place Modification): Write a function move_zeroes(lst) 
    that moves all 0s to the end of the list while maintaining the relative order of the non-zero elements. 
    Constraint: You must modify the list in-place (do not create a new list).
    '''
    #CODE
    zeroes=lst.count(0)
    for i in range(zeroes):
        
           lst.remove(0)
           lst.append(0)
    return lst




if __name__ == "__main__":

    '''
    here you can run what is returned by calling each function separately (uncomment)
    '''

    #print(remove_duplicates([1,2,2,3,4,5,5]))
    #print(chunk_list([1,2,3,4,5,6,7,8],2))
    #print(sort_by_length(["I","like","to","write","code"]))
    #print(move_zeroes([1,3,5,0,7,0,2,4,0,8]))
    pass