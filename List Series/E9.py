list1 = [5, 10, 15, 20, 25, 50, 20]

for i in list1 :
    if i == 20 :
        index = list1.index(i)
        list1.remove(i)
        list1.insert(index, 200)
        break

print(list1)