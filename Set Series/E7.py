set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

if not set1.isdisjoint(set2) :
    print('Two sets have items in common',set1.intersection(set2))
else :
    print('Disjoint')