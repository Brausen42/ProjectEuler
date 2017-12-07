sums_of_powers = []

for n in range(2,1000000):
    remaining = n
    cur_sum = 0
    while remaining != 0:
        cur = remaining % 10
        remaining = remaining // 10
        cur_sum += cur**5
    if cur_sum == n:
        sums_of_powers.append(n)

print(sums_of_powers)
print(sum(sums_of_powers))
