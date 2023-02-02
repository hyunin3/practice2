T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    max_num = arr[0]
    for i in range(1, N):
        if max_num < arr[i]:
            max_num = arr[i]
            
    min_num = arr[0]
    for i in range(1, N):
        if min_num > arr[i]:
            min_num = arr[i] 
            
    print(f'#{tc} {max_num - min_num}')               

###########################

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
 
    mn = 1000000
    mx = 1
    for i in range(N):
        if mx<lst[i]:
            mx=lst[i]
        if mn>lst[i]:
            mn=lst[i]
 
    print(f'#{test_case} {mx-mn}')    