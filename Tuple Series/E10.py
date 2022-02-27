tuple1 = (45, 45, 45, 45)

if len(tuple1) == list(tuple1).count(tuple1[0]) :
    print(True)

print(all(i == tuple1[0] for i in tuple1))