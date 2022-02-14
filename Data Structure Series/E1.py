l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3 = list()
l4 = []

for i in range(1, len(l1), 2) :
    l3.append(l1[i])
for i in range(0, len(l2), 2) :
    l3.append(l2[i])
print(l3)

l4 = l1[1::2]
l4.extend(l2[0::2])
print(l4)