def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow') #10짜리 저장소인데 [10]을 만들라고 하면 만들수 없음
    else:
        stk[top] = item    #그렇지 않으면 거기에 저장

size = 10         #10짜리 stk를 만들겠다
stk = [0]*size 
top = -1          #초기화


    
def pop():
    global top
    if top == -1:   #top이 초기값이면 더 이상 꺼낼게 없음
        print('underflow')
        return 0
    else:
        top -= 1
        return stk[top + 1] #감소시키기 전 좀 전에 내려놓은 애



#스택 구현하고 3개의 데이터 저장한 뒤 다시 꺼내기

stk= [0]*3
top = -1

top += 1
stk[top] = 10

top += 1
stk[top] = 20

top += 1
stk[top] = 30


if top > -1: #꺼낼게 있을 경우에만 꺼내도록
    top -= 1
    stk[top + 1]

if top > 1:
    top -= 1
    stk[top + 1]

if top > -1:
    top -= 1
    stk[top + 1]  #역순으로 30,20,10순으로 나옴