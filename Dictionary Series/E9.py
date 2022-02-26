sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

tiny = min(sample_dict.values())

for i in sample_dict :
    if sample_dict[i] == tiny :
        print(i)

print(min(sample_dict, key=sample_dict.get))

print(min(sample_dict, key = sample_dict.get))