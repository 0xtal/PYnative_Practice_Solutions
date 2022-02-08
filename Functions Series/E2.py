def func1(*args) :
    print('Printing values', end = '\n')
    for i in args :
        print(i)


func1(20, 40, 60)