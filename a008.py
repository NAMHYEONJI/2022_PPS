n = int(input())
for i in range(n):
    score = list(map(int, input().split(' ')))
    avg = sum(score[1:])/score[0]
    cnt = 0
    for s in score[1:]:
        if s > avg:
            cnt += 1
    res = cnt / score[0] * 100
    print(f'{res:.3f}%')