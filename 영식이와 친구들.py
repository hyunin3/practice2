N, M, L = map(int, input().split())
cnt = [0]*(N+1)
s=1
cnt[1] = 1

while True:
    s = s + L
    if s > N:
        s = s - N
        cnt[s] += 1

        if cnt[s] == M:
            break

    else:
        cnt[s] += 1
        ans = 0
        if cnt[s] == M:
            break

print(sum(cnt) - 1)