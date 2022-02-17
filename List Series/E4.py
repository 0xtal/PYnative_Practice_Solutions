list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []

list3 = [list1[0] + list2[0], list1[0] + list2[1], list1[1] + list2[0], list1[1] + list2[1]]

print(list3)

res = [x + y for x in list1 for y in list2]
print(res)