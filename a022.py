n = int(input()) 
li = list(map(int,input().split())) 

y = 0 
m = 0 
for i in li: 
    y += i // 30 * 10 + 10 
    m += i // 60 * 15 + 15 
if y < m: 
    print('Y',y) 
elif y > m: 
    print('M', end=' ') 
    print(m)
else: 
    print('Y M', end= ' ')
    print(y)