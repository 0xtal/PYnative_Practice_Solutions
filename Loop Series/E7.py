i = 5
j = 5
while i > 0 :
    while j > 0 :
        print(j, end = ' ')
        j -= 1
    print()
    i -= 1
    j = i



for i in range(5) :
    for j in range(5-i, 0, -1) :
        print(j, end = ' ')
    print()
