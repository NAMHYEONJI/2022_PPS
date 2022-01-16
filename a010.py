def solution(s):
    res=[]
    if len(s)==1:
        return 1
    for i in range(1, (len(s)//2)+1):
        cnt = 1
        a = ''
        temp=s[0:i]
        for j in range(i, len(s), i):
            if temp == s[j:i+j]:
                cnt += 1
            else:
                if cnt!=1:
                    a = a + str(cnt) + temp
                else:
                    a = a + temp
                
                temp=s[j:j+i]
                cnt = 1
        if cnt!=1:
            a = a + str(cnt) + temp
        else:
            a = a + temp 
        res.append(len(a))

    return min(res)
        