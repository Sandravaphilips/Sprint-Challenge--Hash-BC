#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for i in tickets:
        if i.source == 'NONE':
            route[0] = i.destination
        else:
            hash_table_insert(hashtable, i.source, i.destination)

    index = 1
    while index < length:
        if hash_table_retrieve(hashtable, route[index-1]) == 'NONE':
            pass
        else:
            route[index] = hash_table_retrieve(hashtable, route[index-1])
        index += 1
    return [i for i in route if i]

