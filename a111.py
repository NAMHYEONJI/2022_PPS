n = int(input())
coin_li = [500, 100, 50, 10, 5, 1]

rest = 1000 - n
res = 0

for coin in coin_li:
    res += rest // coin
    rest = rest % coin

print(res)