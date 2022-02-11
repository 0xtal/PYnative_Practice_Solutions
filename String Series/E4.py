str1 = 'PyNaTive'

str2 = ''
for i in str1 :
    if i.islower() :
        str2 += i
for i in str1 :
    if i.isupper() :
        str2 += i

print(str2)