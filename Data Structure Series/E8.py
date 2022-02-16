roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
not_in = []
print(roll_number)

for item in roll_number :
    for value in sample_dict :
        if item == sample_dict[value] :
            found = True

    if not found :
        not_in.append(item)
    found = False

for i in not_in :
    roll_number.remove(i)

print(roll_number)

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
print(roll_number)
roll_number[:] = [item for item in roll_number if item in sample_dict.values()]
print(roll_number)