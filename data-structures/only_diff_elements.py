#!/usr/bin/env python3
def only_diff_elements(set_1, set_2):
    a_set_1 = set()
    b_set_2 = set()

    for element in set_1:
        if element not in set_2:
            a_set_1.add(element)
    for element in set_2:
        if element not in set_1:
            b_set_2.add(element)

    final_set = a_set_1.union(b_set_2)

    return final_set



