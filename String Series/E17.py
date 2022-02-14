from pickle import TRUE


str1 = "Emma25 is Data scientist50 and AI Expert"

count = 0
point = 0

for i in str1 :
    if i.isalpha() :
        letter = TRUE
    if i.isnumeric() :
        number = TRUE
    if str1[count] == (' ') :
        if letter and number :
            print(str1[point:count:])
            letter, number = 0,0
        point = count + 1
    count += 1

if letter and number :
    print(str1[point:count])