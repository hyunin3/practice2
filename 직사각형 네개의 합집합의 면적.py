N = 4
arr = [[0] *10 for _ in range(10)] #arr미리 만들어두고 변수 선언 주의
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] += 1
    cnt = 0
    for lst in arr:
        for n in lst:
            if n >= 1:
                cnt += 1    
        
print(cnt)
