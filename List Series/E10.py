list1 = [5, 20, 15, 20, 25, 50, 20]

for item in list1 :
    if item == 20 :
        list1.remove(item)

print(list1)

list1 = [5, 20, 15, 20, 25, 50, 20]

list1 = [i for i in list1 if i != 20]

print(list1)