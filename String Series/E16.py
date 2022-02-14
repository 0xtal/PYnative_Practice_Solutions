str1 = 'I am 25 years and 10 months old'
str2 = ''

for i in range(len(str1)) :
    if str1[i].isnumeric() :
        str2 = str2 + str1[i]

print(str2)