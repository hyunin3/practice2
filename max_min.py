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
    for i in range(1, N):
        if mx<lst[i]:
            mx=lst[i]
        if mn>lst[i]:
            mn=lst[i]
 
    print(f'#{test_case} {mx-mn}')    

#############################

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    for i in range(N-1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

    a = lst[N-1] - lst[0]
    print(f'#{tc}', a) #버블소트 사용 후 마지막 값에서 첫 값 빼줌