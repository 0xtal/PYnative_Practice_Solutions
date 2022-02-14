str1 = 'Emma-is-a-data-scientist'
count = 0
point = 0

for i in str1 :
    if str1[count] == ('-') :
        print(str1[point:count:])
        point = count + 1
    count += 1
print(str1[point:count])