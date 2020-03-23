#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for index, weight in enumerate(weights):
        hash_table_insert(ht, weight, index)

    i = 0
    while i < length-1:
        difference = limit - weights[i]
        index_of_difference = hash_table_retrieve(ht, difference)
        if index_of_difference is not None:
            if i > index_of_difference:
                return [i, index_of_difference]
            else: return [index_of_difference, i]

        i += 1
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
