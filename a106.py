x = int(input())
n = 0
cnt = 0

while cnt < x:
    n += 1
    cnt += n

cnt -= n

if n % 2 == 0:
    i = x - cnt
    j = n - i + 1
else:
    i = n - (x - cnt) + 1
    j = x - cnt

print(f"{i}/{j}")