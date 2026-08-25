def swap_extremes(lst):
    '''
    Access & Change: Write a function swap_extremes(lst) that takes a list of integers. 
    If the list is empty, return it. Otherwise, swap the first and last elements of the list and return the modified list.
    '''
    #CODE
    if lst:
        lst[0],lst[-1]=lst[-1],lst[0]
        return lst
    return lst

def manage_inventory(inventory,new_item):

    '''
    Add & Remove: Write a function manage_inventory(inventory, new_item). 
    The function should check if the string "Out of Stock" exists in the inventory list. 
    If it does, remove it. Then, append the new_item to the end of the list and return it.
    '''

    #CODE
    
    if "Out of Stock" in inventory:
        #Use 'in' to check existence directly
        inventory.remove("Out of Stock")

    #.append() don't return updated list 
    inventory.append(new_item)

    return inventory
    
def  marge_and_sort(list1,list2):

    '''
    Join & Sort: Write a function merge_and_sort(list1, list2) that takes two lists of numbers, 
    joins them together into a single list, sorts the new list in descending order, and returns it.
    '''
    
    #CODE

    joined_lists=list1+list2
    descending_list=sorted(joined_lists,reverse=True)
    return descending_list

def sum_even_indices(lst):

    '''
    Looping & Access: Write a function sum_even_indices(lst) 
    that loops through a list of numbers and returns the sum of the numbers located specifically at the even indices (index 0, 2, 4, etc.).
    '''

    #CODE

        #short way#
    return sum(lst[::2])

        #long way#
    # total=0
    # for index,number in enumerate(lst):
    #     if index%2==0:
    #         total+=number
    # return total

def  safe_duplicate(lst):

    '''
    Copying Lists: Write a function safe_duplicate(lst). 
    It must create an exact copy of the input list, append the string "COPY" to the end of the new list, 
    and return both lists as a tuple: (original_list, new_list).
    '''

    #CODE

    copy_list=lst.copy()
    copy_list.append("COPY")
    return (lst,copy_list)

def filter_positive_evens(lst):

    '''
    List Comprehension: Write a function filter_positive_evens(lst) 
    that uses a single list comprehension to return a new list containing only the positive, 
    even numbers from the original list.
    '''

    #CODE
    return [number for number in lst if number>0 and number%2==0] 





if __name__ =="__main__":

    #print(swap_extremes([1,2,3]))
    #print(manage_inventory([],""))
    print(filter_positive_evens([-1,-2,2,3,4,5,-6,7,8,-10]))
    #pass