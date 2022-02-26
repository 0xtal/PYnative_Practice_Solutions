set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

common = set1.intersection(set2)
set1.update(set2)
set1.difference_update(common)

print(set1)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.symmetric_difference(set2))