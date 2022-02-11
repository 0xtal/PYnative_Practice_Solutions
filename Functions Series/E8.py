def even_printer(start,end) :
    list = []
    for i in range(start,end) :
        if not i % 2 :
            list.append(i)
    return list
        

print(even_printer(4,30))