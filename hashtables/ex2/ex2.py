#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)
# * We can hash each ticket such that the starting location is the key and the destination is
# the value. Then, when constructing the entire route, the `i`th location in
# the route can be found by checking the hash table for the `i-1`th location.

# ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD"]


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length
    for ticket in tickets:
        hash_table_insert(ht, ticket.source, ticket.destination)
    start = hash_table_retrieve(ht, 'NONE')
    route[0] = start
    for i, r in enumerate(route):
        if i + 1 > len(route) - 1:
            break
        route[i + 1] = hash_table_retrieve(ht, r)

    return route


print(reconstruct_trip(tickets=[
    Ticket(source="PIT", destination="ORD"),
    Ticket(source="XNA", destination="CID"),
    Ticket(source="SFO", destination="BHM"),
    Ticket(source="FLG", destination="XNA"),
    Ticket(source="NONE", destination="LAX"),
    Ticket(source="LAX", destination="SFO"),
    Ticket(source="CID", destination="SLC"),
    Ticket(source="ORD", destination="NONE"),
    Ticket(source="SLC", destination="PIT"),
    Ticket(source="BHM", destination="FLG")
], length=9))
