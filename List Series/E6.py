list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

for i in list1 :
    if not i :
        list1.remove(i)

print(list1)


clean = list(filter(None, list1))

print(clean)