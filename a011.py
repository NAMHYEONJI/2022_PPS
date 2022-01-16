def solution(N, stages):
    f_rate = {}
    reach_user = len(stages)

    for stage in range(1, N+1):
        if reach_user != 0:
            fail_user = stages.count(stage)
            f_rate[stage] = fail_user / reach_user
            reach_user -= fail_user
        else:
            f_rate[stage] = 0

    # res = sorted(f_rate.values(), reverse=True)
    # print(res)
    return sorted(f_rate, key=lambda x : f_rate[x], reverse=True)
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))