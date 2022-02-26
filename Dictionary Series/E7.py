sample_dict = {'a': 100, 'b': 200, 'c': 300}


switch = sample_dict.get(input('What are you looking for: '))

if switch == None :
    print('Not present')
else :
    print(switch, 'present in dict')