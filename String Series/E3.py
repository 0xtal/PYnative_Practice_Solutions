def get_one(str) :
    return str[0]

def get_mid(str) :
    return str[len(str)//2]

def get_end(str) :
    return str[len(str)-1]

def getter(func) :
    return func(s1) + func(s2)

s1 = "America"
s2 = "Japan"

print(getter(get_one) + getter(get_mid) + getter(get_end))
