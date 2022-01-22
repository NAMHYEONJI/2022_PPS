def solution(array, commands):
    answer = []
    for c in commands:
        res_array = array[c[0]-1:c[1]]
        res_array.sort()
        answer.append(res_array[c[2]-1])
    
    return answer