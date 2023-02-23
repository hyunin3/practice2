N = int(input())
lst = list(map(int, input().split()))
alst = []
for i in range(N):
    alst.insert(i-lst[i], i+1)

print(*alst)