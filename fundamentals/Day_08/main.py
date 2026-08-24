def swap_extremes(lst):
    '''
    Access & Change: Write a function swap_extremes(lst) that takes a list of integers. 
    If the list is empty, return it. Otherwise, swap the first and last elements of the list and return the modified list.
    '''
    if lst:
        lst[0],lst[-1]=lst[-1],lst[0]
        
        return lst
    return lst
if __name__ =="__main__":
    #print(swap_extremes([1,2,3]))
    pass