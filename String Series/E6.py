s1 = "Abc"
s2 = "Xyz"

s3 = ''

for i in range(3) :
    s3 = s3 + s1[i]
    s3 = s3 + s2[len(s2)-i-1]

print(s3)