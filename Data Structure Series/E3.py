sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

split = len(sample_list)//3
chunk1 = sample_list[:split]
chunk2 = sample_list[split:2*split]
chunk3 = sample_list[2*split:]

print('Chunk 1:', chunk1)
chunk1.reverse()
print('After reversing it:', chunk1)

print('Chunk 2:', chunk2)
chunk2.reverse()
print('After reversing it:', chunk2)

print('Chunk 3:', chunk3)
chunk3.reverse()
print('After reversing it:', chunk3)