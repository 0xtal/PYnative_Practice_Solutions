str1 = "/*Jon is @developer & musician"
i = 0
switch = False
str2 = ''

for i in range(len(str1)) :
    if str1[i].isalnum() :
        str2 = str2 + str1[i]
        switch = True

    elif str1[i] == ' ':
        if switch :
            str2 = str2 + str1[i]
            switch = False
            
print(str2)