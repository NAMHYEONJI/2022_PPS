def solution(s):
    p_cnt = 0
    y_cnt = 0
    for c in s:
        if c == "P" or c == 'p':
            p_cnt += 1
        elif c == "Y" or c == 'y':
            y_cnt += 1
    if p_cnt == y_cnt:
        return True
    return False