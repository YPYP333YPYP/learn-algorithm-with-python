from ast import Pass
from typing import Any

from matplotlib.pyplot import vlines

class FixedStack: 

    class Empty(Exception): # 스택이 가득 찼을 때 예외 처리 클래스
        pass

    class Full(Exception): # 스택이 비어 있을 때 예외 처리 클래스
        pass

    def __init__(self, capacity:int = 256) -> None:
        self.capacity = capacity # 스택의 크기
        self.stk = [None] * capacity # 스택의 본체
        self.ptr = 0 # 스택의 데이터 개수

    def __len__(self) -> int: # 스택의 데이터 개수 알아내는 함수
        return self.ptr
    
    def is_empty(self) -> bool: # 스택이 비어있는지 확인하는 함수
        return self.ptr <= 0
    
    def is_full(self) -> bool: # 스택이 가득 찼는지 확인하는 함수
        return self.ptr >= self.capacity

    """ 예외 처리 클래스를 사용"""    
        
    def push(self, value:Any) -> None: # 스택에 데이터 추가
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any: # 스택에 데이터를 꺼내 반환
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def peek(self) -> Any: # 스택의 Top 데이터를 꺼내 반환
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]

    def clear(self) -> None: # 스택의 모든 데이터 삭제
        self.ptr = 0

    def find(self, value:Any) -> Any: # 스택의 데이터를 찾아서 반환 
        for i in range((self.ptr - 1), -1, -1): # 스택의 꼭대기 부터 스택의 바텀(인덱스 0) 까지 스캔
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value:Any) -> int: # 데이터의 개수를 파악
        c = 0
        for i in range(self.ptr):
            if self.str[i] == value:
                c +=1 
        return c

    def __contains__(self,value:Any) -> bool: # 데이터가 들어 있는지 확인
        return self.count(value) > 0
    
    def dump(self) -> None: # 스택을 출력
        if self.is_empty():
            print('스택이 비어있습니다')
        else:
            print(self.stk[:self.ptr])
    


from enum import Enum


Menu = Enum('Menu', ['푸시', '팝', '피크', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '   ', end='')
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)

s = FixedStack(64)  # 최대 64개를 푸시할 수 있는 스택

while True:
    print(f'현재 데이터 개수: {len(s)} / {s.capacity}')
    menu = select_menu()  # 메뉴 선택
    
    if menu == Menu.푸시:  # 푸시
        x = int(input('데이터를 입력하세요.: '))
        try:
            s.push(x)
        except FixedStack.Full:
            print('스택이 가득 차 있습니다.')

    elif menu == Menu.팝:  # 팝
        try:
            x = s.pop()
            print(f'팝한 데이터는 {x}입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')

    elif menu == Menu.피크:  # 피크
        try:
            x = s.peek()
            print(f'피크한 데이터는 {x}입니다.')
        except FixedStack.Empty:
            print('스택이 비어 있습니다.')

    elif menu == Menu.검색:  # 검색
        x = int(input('검색할 값을 입력하세요.: '))
        if x in s:
            print(f'{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.')
        else:
            print('검색값을 찾을 수 없습니다.')

    elif menu == Menu.덤프:  # 덤프
        s.dump()

    else:
        break   