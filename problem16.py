s = pow(2,1000)
add = 0
for i in range(0,1000):
    add += s % 10
    s = s//10
print(add)
