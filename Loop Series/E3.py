def sequential(high) :
    sum = 0
    for i in range(high+1) :
        sum = sum + i
    print('Sum is:', sum) 


top = int(input('Provide an integer: '))
sequential(top)