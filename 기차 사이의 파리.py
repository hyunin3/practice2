T = int(input())
for tc in range(1, T + 1):
    D, A, B, F = map(int, input().split())
    t = D / (A + B) #기차가 충돌하기까지의 시간(파리가 죽기까지의 시간)
    print(f'#{tc} {F*t}') #파리는 어차피 죽기전까지 등속운동을 함