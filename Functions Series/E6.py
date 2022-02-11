def recurse(n) :
    if n <= 1 :
        return n
    else :
        return n + recurse(n-1)


out = recurse(int(input('Enter a postive number: ')))
print(out)