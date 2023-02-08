def BruteForce(p, t):  #p는 찾을 패턴, t는 전체 텍스트
    i = 0  # t의 인덱스
    j = 0  # p의 인덱스
    while j < len(p) and i < len(t):
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == len(p):
        return 1  # 검색성공
    else:
        return 0  # 검색실패

T = int(input())
for tc in range(1, T + 1):
    N = str(input())
    M = str(input())
    print(f'#{tc} {BruteForce(N, M)}')