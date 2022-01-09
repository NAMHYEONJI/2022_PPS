max = 0
max_idx = 0
for i in range(1,6):

    li = list(map(int, input().split()))
    s = sum(li)
    if max < s:
        max = s
        max_idx = i
print(max_idx, max)