def solution(people, limit): 
    answer = 0 
    people.sort() 
    first, last = 0, len(people) - 1 
    while first <= last: 
        answer += 1 
        if people[first] + people[last] <= limit: 
            first += 1 
        last -= 1 
    return answer

