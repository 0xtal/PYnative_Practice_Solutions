from random import randint



chance = randint(0,1)


if chance :
    checkempty = open('E9_file_check.txt', 'w')
    checkempty.write('superduper')
    checkempty.close()

checkempty = open('E9_file_check.txt', 'r')

checkempty.close()