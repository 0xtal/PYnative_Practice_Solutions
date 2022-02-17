list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

sub_list = ["h", "i", "j"]

for i in sub_list :
    list1[2][1][2].append(i)

print(list1)

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

list1[2][1][2].extend(sub_list)

print(list1)