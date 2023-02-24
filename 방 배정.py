N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
f = []
m = []
cnt1 = [0]*7
cnt2 = [0]*7

for lst in arr:
    if lst[0] == 0:
        f.append(lst[1])
    else:
        m.append(lst[1])

for n in f:
    for i in range(7):
        if n == i:
            cnt1[i] += 1

for i in range(1, 7):
    if 0 < cnt1[i] <= K:
        cnt1[i] = 1
for i in range(1, 7):
    if cnt1[i] > K:
        cnt1[i] = cnt1[i] // K + 1

for n in m:
    for i in range(7):
        if n == i:
            cnt2[i] += 1

for i in range(1, 7):
    if 0 < cnt2[i] <= K:
        cnt2[i] = 1
for i in range(1, 7):
    if cnt2[i] > K:
        cnt2[i] = cnt2[i] // K + 1

print(sum(cnt1)+sum(cnt2))