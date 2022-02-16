roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
not_in = []

for item in roll_number :
    for value in sample_dict :
        if item == sample_dict[value] :
            found = True

    if not found :
        not_in.append(item)
    found = False

print(not_in)
for i in not_in :
    roll_number.remove(i)

print(roll_number)