def solution(s):
    answer = '' 
    words = s.split(' ')
    for i in range(len(words)): 
        words[i] = words[i].capitalize() 
    answer = ' '.join(words) 
    return answer

# solution("3people unFollowed me")
# solution("for the last week")