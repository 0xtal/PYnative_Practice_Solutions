str1 = '/*Jon is @developer & musician!!'
str2 = ''

for i in range(len(str1)) :
    if not (str1[i].isalnum() or str1[i].isspace()) :
        str2 = str2 + '#'
    else :
        str2 = str2 + str1[i]

print('Old:',str1)
print('New:',str2)