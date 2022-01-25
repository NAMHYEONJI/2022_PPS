n = int(input())

for i in range(n) :
  li = [0] * 27
  value = input()
  for j in range(len(value)) :
    li[int(ord(value[j]))-65] += 1

  res = 0
  for i in range(26) :
    if li[i] == 0 :
      res += i + 65

  print(res)