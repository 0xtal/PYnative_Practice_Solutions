numbers = [12, 75, 150, 180, 145, 525, 50]

for item in numbers :
    if not item % 5 :
        if item > 500 :
            break
        if item > 150 :
            continue
        print(item)
        