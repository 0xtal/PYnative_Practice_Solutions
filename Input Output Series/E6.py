source = open('E6_data_in.txt', 'r')
source_line = source.read()
source.close()

print(source_line)
print('\n',end='')
source_line = source_line.replace('line5\n','')

destination = open('E6_data_out.txt', 'w')
destination.write(source_line)
destination.close()

destination = open('E6_data_out.txt', 'r')
for line in destination :
    print(line, end = '')

destination.close()

