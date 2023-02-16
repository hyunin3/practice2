tbl = [0, 2, 3, 1]


def solve(s, e):
    # 1명만 남으면 승부없이 종료
    if s == e:
        return s  # 승리자의 idx return

    # [1] 좌/우 그룹에서 각각의 승자 찾기
    a = solve(s, (s + e) // 2)
    b = solve((s + e) // 2 + 1, e)

    # [2] 단위작업    
    if tbl[lst[a]] == lst[b]:  # b가 승리
        return b
    return a  #아니면 a가 승리

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [0] + list(map(int, input().split()))

    ans = solve(1, N)
    print(f'#{tc} {ans}')