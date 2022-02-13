str1 = 'Apple'

unique = ''
unset = {}

#identifies unique characters
for i in str1 :
    if unique.find(i) < 0 :
        unique = unique + i

#create dictionary
for i in unique :
    unset[i] = str1.count(i)

print(unset)