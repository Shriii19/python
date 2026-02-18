def avg (a,b,c,d):
    return a+b+c+d/4
sum =avg(1,2,3,4)
print(sum)

#method 2
def calcavg(a,b,c):
    sum = a+b+c
    avg =sum/3
    print(avg)
    return avg

total = calcavg(1,2,3)
