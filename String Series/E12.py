str1 = "Emma is a data scientist who knows Python. Emma works at google."

pointer = 0
next = 0

pointer = str1.find('Emma')

if str1.count('Emma') > 1 :
    for i in range(1, str1.count('Emma')) :
        pointer = str1[next + 1::].find('Emma')
        next = pointer + next + 1
        print(pointer,next,i)
        

print('Last occurrence of Emma starts at index', next)