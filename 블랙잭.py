N, M = map(int, input().split())
lst = list(map(int, input().split()))
sum = 0
alst = []
for i in range(N-2):       # N개 중 3개를 뽑는 조합 구하기!  
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = lst[i]+lst[j]+lst[k]

            alst.append(sum)
#print(alst)
alst.sort()
ans = 0
for i in range(len(alst)):
    if alst[i] > M:
        ans = alst[i-1]
        break

print(ans)