str1 = "P@#yn26at^&i5ve"

chars, digs, symb = 0,0,0

for i in str1 :
    if i.isalpha() :
        chars += 1
    elif i.isnumeric() :
        digs += 1
    else :
        symb += 1

print("Chars =", chars, "\nDigits =", digs, '\nSymbol =', symb)