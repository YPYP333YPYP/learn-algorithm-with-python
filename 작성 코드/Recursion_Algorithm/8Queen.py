pos = [0] * 8          # 각 열에 배치한 퀸의 위치

""" 해설 : 만약 퀸을 아무런 규칙 없이 배열 한다고 가정하면 64 x 63 x ... x 57 = 178,462,987,637,760 의 경우의 수가 나온다 
    일단 0~7번째 열에다가 퀸을 하나씩 배열한다고 가정하자 pos[i] = j 의 뜻은 i열, j행에 배치된 퀸의 위치를 의미한다. 
    즉 pos[0] = 0 은 0열 0행에 배치된 퀸을 의미한다. pos = [0] * 8 의 의미는 각 열마다 퀸을 한개씩 배치했다는 것을 의미한다. 
    """
flag = [False] *8    
def put() -> None:
    """각 열에 놓은 퀸의 위치를 출력"""
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:
    """i 열의 알맞은 위치에 퀸을 배치"""
    for j in range(8):
        if not flag[j]:  # j 행에 퀸을 배치하지 않았으면
            pos[i] = j   # 퀸을 j 행에 배치
            if i == 7:   # 모든 열에 퀸을 배치를 완료
                put()
            else:
                flag[j] = True
                set(i + 1)  # 다음 열에 퀸을 배치
                flag[j] = False
         
""" 위의 코드에서 set(0)은 0열에 퀸을 1개 배치했다는 것을 의미한다. set(i+1) 의 재귀 함수를 이용해서 0~7열까지 배치를 완료한다 
    배치를 완료하고 put() 함수를 사용하면 조합이 열거 된다    
    이런 식으로 배치 조합을 열거 해 나가는 것을 '분기(branching) 작업 이라고 한다.
    이때 else 부분의 flag 부분을 보면 일종의 분기를 한정 시킬 수 있는데 이 한정된 부분은
    ' 각 행에 퀸을 1개만 배치한다' 라는 부분이다.  
    """

pos = [0] * 8          # 각 열에 배치한 퀸의 위치    
flag_a = [False] * 8   # 각 행에 퀸을 배치했는지 체크
flag_b = [False] * 15  # 대각선 방향(↙↗)으로 퀸을 배치했는지 체크
flag_c = [False] * 15  # 대각선 방향( ↘↖)으로 퀸을 배치했는지 체크

def put() -> None:
    """퀸을 놓는 상황을 □와 ■로 출력"""
    for j in range(8):
        for i in range(8):
            print('■' if pos[i] == j else '□', end='')
        print()
    print()



def set(i: int) -> None:
    """i 열의 알맞은 위치에 퀸을 놓기"""
    for j in range(8):
        if(     not flag_a[j]           # j 행에 아직 퀸을 놓지 않았으면
            and not flag_b[i + j]       # 대각선 방향(↙↗)으로 퀸이 배치 되지 않았다면
            and not flag_c[i - j + 7]): # 대각선 방향( ↘↖)으로 퀸이 배치 되지 않았다면
            pos[i] = j          # 퀸을 j 행에 놓기
            if i == 7:          # 모든 열에 퀸을 배치하는 것을 완료
                put()
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set(i + 1)      # 다음 열에 퀸을 놓기
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False

set(0)          # 0 열에 퀸을 놓기

""" 필요하지 않은 분기를 없애서 필요한 조합을 열거하지 않는 방법을 '한정(bounding) 작업' 이라고 한다.
    분기 작업과 한정 작업을 조합하여 문제를 풀이하는 것을 분기한정법(branching and bounding method) 라고 한다.
    앞서 설정된 flag를 flag_a, flag_b, flag_c로 나눌 건데 각각 행, 대각선 방향(1)(↙↗), 대각선 방향(2)(↘↖)에 대한 한정 작업을 의미한다.
    Flase와 True 의 의미는 True인 곳은 퀸을 배치할 수 없고 False인 곳에는 퀸을 배치할 수 있다.
    """