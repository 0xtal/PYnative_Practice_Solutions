set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set2.update(set1.difference(set2))
print(set2)