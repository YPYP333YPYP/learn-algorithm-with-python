# 재귀 알고리즘 분석

# 상향식 분석과 하향식 분석을 알기 위한 재귀 함수
def recur(n: int) -> int:
    
    if n > 0:
        recur(n - 1)
        print(n)
        recur(n - 2)



# 재귀 알고리즘의 비재귀적 표현
def recur(n: int) -> int:
   
    while n > 0:
        recur(n - 1)
        print(n)
        n = n - 2 

""" 해설 : recur(n-2) 는 곧 n을 업데이트 해주는 방법으로 비재귀적 표현으로 바꿀 수 있다 하지만 recur(n-1)의 비재귀적 표현은 어려운데
    이는 n값을 출력하기 전에 recur(n-1)을 실행해줘야 하기 때문이다. 예를 들어 n의 값이 4라면 recur(3)을 실행하기전에 print(4)를 실행할
    4를 어딘가에 저장해놔야 한다. 이 부분은 스택을 사용한다."""


from stack_copy import Stack  # stack.py의 Stack 클래스를 임포트

def recur(n: int) -> int:
    """재귀를 제거한 함수 recur"""
    s = Stack(n)

    while True:
        if n > 0:
            s.push(n)         # n 값을 푸시
            n = n - 1
            print(f'n-1로 업데이터 된 값 : {n} ')
            continue
        if not s.is_empty():  # 스택이 비어 있지 않으면
            n = s.pop()       # 저장하고 있는 값을 n에 팝
            print(f'출력된 값 : {n} ')
            n = n - 2
            print(f'n-2로 업데이터 된 값 : {n} ')
            continue
        break

""" 해설 : 위 상황의 예를 들어 n=4 일경우에 n값인 4를 스택에 푸시한다. 그 다음 n-1한 값인 3을 만들고 이 과정을 통해 2, 1 까지 스택에 푸시 된 후
    0이 되어 1번 조건에서 벗어난다. 이후 1, 2, 3 의 값이 2번째 조건에 의해서 팝되고 동시에 출력된다. 이때 1과 2과정을 보면 
    그 다음 n-2를 해주면 -1, 0이 나오는데 이 값은 n > 0조건에맞지 않고 넘어가게 된다 그렇게 3이 팝 될때 n-2값이 1이 나오고 이 값은 n > 0 조건에 일치 함으로
    n = 1 값을 다시 푸시한다. 이런식으로 반복하다보면 비재귀적 표현으로 재귀 함수를 표현할 수 있다. """

recur(4)