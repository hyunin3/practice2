T = int(input())
 
code_table = {
    (0, 0, 0, 1, 1, 0, 1): 0,
    (0, 0, 1, 1, 0, 0, 1): 1,
    (0, 0, 1, 0, 0, 1, 1): 2,
    (0, 1, 1, 1, 1, 0, 1): 3,
    (0, 1, 0, 0, 0, 1, 1): 4,
    (0, 1, 1, 0, 0, 0, 1): 5,
    (0, 1, 0, 1, 1, 1, 1): 6,
    (0, 1, 1, 1, 0, 1, 1): 7,
    (0, 1, 1, 0, 1, 1, 1): 8,
    (0, 0, 0, 1, 0, 1, 1): 9,
}
 
 
def find_code():
    global ans
    
    for r in range(N):
        for c in range(M - 1, 55, -1):      #뒤에서부터 봐서 1이 나오면 암호코드. 코드는 56자
            code = arr[r][c:c - 56:-1]
           
            if code[0] != 1:
                continue
 
            # 현재 행 r 에서 시작해서 5개가 다 똑같은지 검사
            for _ in range(r, r + 5):
                ncode = code
                if ncode != code:
                    break
            # 만약 중간에 break 된적이 없으면 5줄이 동일
            else:
             
                code = code[:: -1]
                # 뒤집고 나서 7개씩 8번 쪼갠다.
                # 홀수 * 3 , 짝수는 그냥 +
                code_valid = 0
                # 위의 결과 10의 배수이면, 숫자를 더하기 
                code_sum = 0
                for i in range(8):
                    ni = 7 * i
                    # 코드를 해독한 결과가 테이블(딕셔너리)안에 존재하면 올바른 암호코드
                    decode = code_table.get(tuple(code[ni:ni + 7]))
                    if decode == None:
                        break
                    else:
                        # 코드에 맞는 숫자를 찾았다.
                        # 홀수번째 => * 3 (인덱스는 짝수)
                        # 짝수번쨰 => + (인덱스는 홀수)
                        code_sum += decode
                        if i % 2 == 0:
                            code_valid += decode * 3
                        else:
                            code_valid += decode
                # 중간에 못찾은 코드 없으면 다 코드 후보
                else:
                    # 주어진 식의 결과를 통해 10의 배수이면 코드
                    if code_valid % 10 == 0:
                        ans = code_sum
                      
                        return
 
 
for tc in range(1, T + 1):
    N, M = map(int, input().split())
 
    arr = [list(map(int, input())) for _ in range(N)]
 
    ans = 0
 
    find_code()
 
    print(f"#{tc} {ans}")