sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

unique_list = list(set(sample_list))
print('unique items', unique_list)

unique_tuple = tuple(unique_list)
print('tuple', unique_tuple)

print('min', min(unique_tuple))
print('max', max(unique_tuple))
