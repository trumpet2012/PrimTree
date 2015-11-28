import random


def create_node_associations(num_nodes):
    associations = ()
    for node_index in range(0, num_nodes):
        num_associations = random.randint(1, 2)
        for association in range(1, num_associations+1):
            node_pos = node_index
            while node_pos == node_index:
                node_pos = random.randint(0, num_nodes - 1)

            associations += ((node_index, node_pos), )

    return associations
