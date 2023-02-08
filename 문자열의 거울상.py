T = int(input())
for tc in range(1, T + 1):
    N = str(input())
    N = N[::-1] #문자열 뒤집기
    # 문자열 역순으로 하고 p는 q로 b는 d로
    mirror = str.maketrans('pqbd', 'qpdb')
    print(f'#{tc} {N.translate(mirror)}')
    
    # N = list(input())
    # N = N[::-1]
    # for i in range(len(N)):
    #     if N[i] == 'p':
    #         N[i] = 'q'
    #     elif N[i] == 'q':
    #         N[i] = 'p'
    #     elif N[i] == 'b':
    #         N[i] = 'd'
    #     elif N[i] == 'd':
    #         N[i] = 'b'
    # N = ''.join(N)