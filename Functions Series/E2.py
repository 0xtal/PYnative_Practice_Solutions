from argparse import ArgumentError


def func1(*args) :
    sum = 0
    for i in args :
        sum = sum + i
    print(sum)


func1(20, 40, 60)