m = int(input())
zero = 0
one = 1
for i in range(m) :
    a, b, dir = map(int, input().split())
    zero = zero ^ dir
    one = one // a * b
print(zero, one)
