import sys
sys.stdin = open("input.txt", "r")
N, M, L = map(int, input().split())
cnt = [0]*(N+1)
s=1
cnt[1] = 1
if M == 1:
    print(0)
else:
    while True:
        s = s + L
        if s > N:
            s = s - N
            cnt[s] += 1
            if cnt[s] == M:
                break

        else:
            cnt[s] += 1
            if cnt[s] == M:
                break

    print(sum(cnt) - 1)