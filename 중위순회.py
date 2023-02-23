def inord(n):
    if n*2 <= N:
        inord(n*2)
    alst.append(ch[n])    
    
    if (n*2 + 1) <= N:
        inord(n*2 + 1)               
        
  
T = 10
for tc in range(1, T+1):
    N = int(input())
    
    ch = [0]*(N+1)
    
    for i in range(N):
        lst = list(input().split())
        ch[int(lst[0])] = lst[1]
        
    alst = []
    inord(1)
    print(f'#{tc}', ''.join(alst))