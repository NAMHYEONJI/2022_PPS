import sys

n = int(sys.stdin.readline())
sum = 1
for i in range(n):
    temp = int(sys.stdin.readline())
    sum += temp

print(sum-n)