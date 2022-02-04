#prime number generator

def prime(inp) :
    j = 2
    flag = 0
    while j < i :
        if not i % j :
            flag = 1
            break
        j += 1
    return(flag)
        



for i in range (2,111) :
    effect = prime(i)
    if not effect :
        print(i)