dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

dictf = dict1.copy()
print(dictf)
dictf.update(dict2)
print(dictf)