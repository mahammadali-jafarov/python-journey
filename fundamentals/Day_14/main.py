def find_missing_ids(id_list):

    '''
    Write a function find_missing_ids(id_list) 
    that takes an unsorted list of positive integers where the maximum value in the list represents N. 
    The sequence should ideally run from 1 to N. Return a set containing all missing integers in that range.
    '''
    #CODE
    # 1. Find N (the highest number)
    N = max(id_list)
    
    # 2. Create the "perfect" set from 1 to N
    # We use N + 1 because range() stops one number short!
    perfect_set = set(range(1, N + 1))
    
    # 3. Convert our actual list to a set
    actual_set = set(id_list)
    
    # 4. Subtract the actual numbers from the perfect numbers 
    # to find what is missing (Symmetric Difference or just Minus - )
    return perfect_set - actual_set

    
def jaccard_similarity(doc1,doc2):

    '''
    Write a function jaccard_similarity(doc1, doc2) 
    that takes two string documents and calculates their Jaccard similarity coefficient based on unique words.
    Convert both strings to lower case and split them into sets of words using .split().
    Calculate the Jaccard similarity: |A & B|/|A | B|
    (the number of shared unique words divided by total unique words across both documents).
    Return the resulting float value between 0.0 and 1.0 (handle division by zero by returning 0.0 if both sets are empty).
    '''
    #CODE
    word1=set(doc1.lower().split())
    word2=set(doc2.lower().split())
    shared=word1&word2
    total=word1|word2
    if len(total)==0:
        return "zero division"
    elif doc1==" " and doc2==" ":
        return 0.0
    else:
        return len(shared)/len(total)


if __name__ == "__main__":
    # Exercise : find_missing_ids
    print("--- Exercise 13: The Missing IDs ---")
    print(find_missing_ids([1, 2, 4, 7]))  
    # Expected: {3, 5, 6}

    # Exercise : jaccard_similarity
    print("\n--- Exercise 14: Document Similarity ---")
    doc_a = "Python is a great programming language"
    doc_b = "Python is a popular language for data"
    print(jaccard_similarity(doc_a, doc_b))  
    # Shared: {'python', 'is', 'a', 'language'} (4)
    # Total unique: {'python', 'is', 'a', 'great', 'programming', 'language', 'popular', 'for', 'data'} (9)
    # Expected: 4 / 9 = ~0.4444...

    print(jaccard_similarity("   ", ""))  
    # Expected: 0.0
    