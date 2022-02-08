count = input('How many terms?: ')

reps = ''
sum = 0
for i in range(int(count)) :
    reps = reps + '2'
    sum = sum + int(reps)
print(sum)