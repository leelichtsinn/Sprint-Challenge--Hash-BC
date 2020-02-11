#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)

    """
    YOUR CODE HERE
    """
    answer = []

    for weight in weights:
        # if hash_table_retrieve is None
        if hash_table_retrieve(ht, weight) is None:
            hash_table_insert(ht, weight, (limit-weight))

    print(ht.storage.items())

    # loop through ht to compare keys to value to find the pair that equal the limit
    # for index in ht.storage:
    #     print(ht.storage[index])
    # return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

w = [ 4, 6, 10, 15, 16 ]
length = 5
limit = 21

get_indices_of_item_weights(w, length, limit)
