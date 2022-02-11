str1 = "PYnative29@#8496"

sum, count = 0,0
for i in str1 :
    if i.isnumeric() :
        sum += int(i)
        count += 1
print(sum)
print(sum/count)
