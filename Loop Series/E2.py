from re import I


i,j = 1,2

while j <= 6 :
    while i < j :
        print(i, end = ' ')
        i += 1
    print('\n', end = '')
    i = 1
    j += 1