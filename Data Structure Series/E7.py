
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

#if either is a subset, the other is a superset

if not first_set.difference(second_set) :
    print('First set is Subset. Second set is Superset.')
elif not second_set.difference(first_set) :
    print('First set is Superset. Second set is Subset.')
else :
    print('Neither is Subset/Superset')