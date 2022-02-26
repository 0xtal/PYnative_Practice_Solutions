from logging.config import dictConfig


sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

dict2 = {}
for i in keys :
    dict2[i] = sample_dict[i]

print(dict2)

newDict = {i: sample_dict[i] for i in keys}
print(newDict)