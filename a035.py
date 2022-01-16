n = int(input())

for i in range(n):
    li = list(input().split())
    res = float(li[0])
    for i in range(len(li)):
        if li[i] == '@':
            res *= 3
        elif li[i] == '%':
            res += 5
        elif li[i] == '#':
            res -= 7
    
    print("%0.2f" % res)