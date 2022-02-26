employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

dict2 = {}
for i in employees :
    dict2[i] = defaults

print(dict2)

new = dict.fromkeys(employees,defaults)
print(new)
print(new['Emma'])