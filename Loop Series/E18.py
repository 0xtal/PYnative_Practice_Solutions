n = 5

star = '* '
for i in range(n) :
    print(star, end = '\n')
    star = star + '* '

for i in range(n-1, 0, -1) :
    print(star[0:i*2], end = '\n')
