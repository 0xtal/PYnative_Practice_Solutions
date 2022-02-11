def check(s1,s2) :
    return s2.find(s1)

if check("Yn", "PYnative") > 0 :
    print('True')
else :
    print('False')

if check("Ynf", "PYnative") > 0:
    print('True')
else :
    print('False')