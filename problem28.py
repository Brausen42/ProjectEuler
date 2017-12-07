cur = 1
total = 1

for n in range(2,1001,2):
    for i in range(4):
        cur += n
        total += cur

print(total)
