import sys, math

n = int(input().strip())
count = 0
maxi = 0
while n > 0:
    if n % 2 == 1:
        count += 1
    else:
        if count > maxi:
            maxi = count
        count = 0
    n=math.floor(n / 2)
if count > maxi:
    maxi = count
print(maxi)
    