from random import randint

checkempty = open('E9_file_check.txt', 'w')
checkempty.write('')
checkempty.close()

chance = randint(0,1)

if chance :
    checkempty = open('E9_file_check.txt', 'w')
    checkempty.write('stuff')
    checkempty.close()

checkempty = open('E9_file_check.txt', 'r')
checkempty_line = checkempty.read()
checkempty.close()

if not len(checkempty_line) :
    print('File is empty')
else :
    print('File is not empty')