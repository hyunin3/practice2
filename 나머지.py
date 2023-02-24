T = 10
cnt = 0
ans = 0
lst = []
for tc in range(1, T + 1):
    N = int(input())
    a = N % 42
    lst.append(a)
lst.sort()
for i in range(len(lst)-1):
    if lst[i] != lst[i+1]:
        cnt += 1
if cnt == 0:
    ans = 1
else:
    ans = cnt + 1
print(ans)