sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for i in keys :
    del sample_dict[i]

print(sample_dict)

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

for i in keys :
    sample_dict.pop(i)
print(sample_dict)

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sample_dict = {i: sample_dict[i] for i in sample_dict.keys()-keys}
print(sample_dict)