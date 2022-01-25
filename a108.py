a,b = map(int, input().split())

li = []
i = 1
while(True):
  if len(li) > 1000 :
    break
  li += [i] * i
  i += 1


print(sum(li[a-1:b]))