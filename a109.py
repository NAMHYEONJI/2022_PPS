n = int(input())
for i in range(n):
    num = input()
    rev_num = num[::-1]
    sum = int(num)+int(rev_num)
    check = True
    sum = str(sum)
    for j in range(int(len(sum)/2)):
      if sum[j] != sum[len(sum)-j-1]:
        check = False
    if check :
      print("YES")
    else:
      print("NO")
