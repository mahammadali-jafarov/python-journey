def get_capital(country_dict,country):


    '''
    Accessing: Write a function get_capital(country_dict, country). 
    If the country (key) exists in the dictionary, return its capital (value). 
    If it does not exist, return the string "Not Found". (Hint: Look up the .get() method).
    '''
    #CODE
    return country_dict.get(country,"Not Found")

def update_score(player_scores,player,new_score):

    '''
    Updating: Write a function update_score(player_scores, player, new_score). 
    If the player exists, update their score. If they do not exist, 
    add them to the dictionary with the new score. Return the dictionary.
    '''

    #CODE
    player_scores[player]=new_score
    return player_scores

def remove_outlier(data_dict,key_to_remove):

    ''' 
    Removing: Write a function remove_outlier(data_dict, key_to_remove). 
    If the key exists, safely remove it from the dictionary. Return the modified dictionary.
    '''
    #CODE
    data_dict.pop(key_to_remove,None)
    return data_dict


def check_inventory(invenrtory_dict,item):

    '''
    Existence: Write a function check_inventory(inventory_dict, item). 
    Return True if the item exists as a key and its value is greater than 0. Otherwise, return False.
    '''
    #CODE
    return item in invenrtory_dict and invenrtory_dict[item]>0 



def sum_all_values(financial_dict):

    '''
    Looping: Write a function sum_all_values(financial_dict) 
    that loops through the dictionary and returns the total sum of all the values.
    '''
    #CODE
    # short way
    # return sum(financial_dict.values())
    total=0
    for value in financial_dict.values():
        total+=value
    return total
    


if __name__ =="__main__":

    # Exercise 1: get_capital
    print("--- Exercise 1 ---")
    print(get_capital({"France": "Paris", "Japan": "Tokyo"}, "Japan"))  # Expected: Tokyo
    print(get_capital({"France": "Paris"}, "Italy"))                    # Expected: Not Found

    # Exercise 2: update_score
    print("\n--- Exercise 2 ---")
    print(update_score({"Alice": 10}, "Bob", 20))    # Expected: {'Alice': 10, 'Bob': 20}
    print(update_score({"Alice": 10}, "Alice", 15))  # Expected: {'Alice': 15}

    # Exercise 3: remove_outlier
    print("\n--- Exercise 3 ---")
    print(remove_outlier({"a": 1, "b": 2, "outlier": 99}, "outlier")) # Expected: {'a': 1, 'b': 2}
    print(remove_outlier({"a": 1, "b": 2}, "missing"))                # Expected: {'a': 1, 'b': 2}

    # Exercise 4: check_inventory
    print("\n--- Exercise 4 ---")
    print(check_inventory({"apples": 5, "bananas": 0}, "apples"))   # Expected: True
    print(check_inventory({"apples": 5, "bananas": 0}, "bananas"))  # Expected: False (value is not > 0)
    print(check_inventory({"apples": 5}, "oranges"))                # Expected: False (key missing)

    # Exercise 5: sum_all_values
    print("\n--- Exercise 5 ---")
    print(sum_all_values({"rent": 1000, "groceries": 300}))         # Expected: 1300