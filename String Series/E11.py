str1 = "PYnative"
str2 = ''

for i in range(len(str1), 0, -1) :
    str2 = str2 + str1[i-1]

print(str2)