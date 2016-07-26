onesCounts = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}
tensCounts = {0:0,1:4,2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}
hundred = 7
thousand = 8
letterSum = 0
count = 1

def onesPlace(n):
    return n%10
def tensPlace(n):
    return (n//10)%10
def hundredsPlace(n):
    return (n//100)%10

def getValue(n):
    global count
    if n == 10:
        return 3
    elif n == 11 or i == 12:
        return 6
    elif n == 13:
        return 8
    elif n == 15:
        return 7
    elif n == 18:
        return 8
    elif n == 1000:
        return 11
    else:
        letterCount = 0
        if hundredsPlace(n) == 0:
            letterCount += onesCounts[onesPlace(n)]
            letterCount += tensCounts[tensPlace(n)]
        else:
            letterCount += 7
            letterCount += onesCounts[hundredsPlace(n)]
            if not(onesPlace(n) == 0 and tensPlace(n) == 0):
                letterCount += 3
                letterCount += getValue(n%100) 
        return letterCount

for i in range(1,1001):
    letterSum += getValue(i)
print(letterSum)


