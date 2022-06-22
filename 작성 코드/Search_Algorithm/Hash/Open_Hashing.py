

from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib

# 버킷의 속성
class Status(Enum):
    OCCUPIED = 0  # 데이터를 저장
    EMPTY = 1     # 비어 있음
    DELETED = 2   # 삭제 완료

class Bucket:
    """해시를 구성하는 버킷"""

    def __init__(self, key: Any = None, value: Any = None,
                       stat: Status = Status.EMPTY) -> None:
        """초기화"""
        self.key = key      # 키
        self.value = value  # 값
        self.stat = stat    # 속성

    def set(self, key: Any, value: Any, stat: Status) -> None:
        """모든 필드에 값을 설정"""
        self.key = key      # 키
        self.value = value  # 값
        self.stat = stat    # 속성

    def set_status(self, stat: Status) -> None:
        """속성을 설정"""
        self.stat = stat

class OpenHash:
    """오픈 주소법을 구현하는 해시 클래스"""

    def __init__(self, capacity: int) -> None:
        """초기화"""
        self.capacity = capacity                 # 해시 테이블의 크기를 지정
        self.table = [Bucket()] * self.capacity  # 해시 테이블

    def hash_value(self, key: Any) -> int:
        """해시값을 구함"""
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.md5(str(key).encode()).hexdigest(), 16)
                % self.capacity)

    def rehash_value(self, key: Any) -> int:
        """재해시값을 구함"""
        return(self.hash_value(key) + 1) % self.capacity

    def search_node(self, key: Any) -> Any:
        """키가 key인 버킷을 검색"""
        hash = self.hash_value(key)  # 검색하는 키의 해시값
        p = self.table[hash]         # 버킷을 주목

        for i in range(self.capacity):
            if p.stat == Status.EMPTY:
                break
            elif p.stat == Status.OCCUPIED and p.key == key:
                return p
            hash = self.rehash_value(hash)  # 재해시
            p = self.table[hash]
        return None

    def search(self, key: Any) -> Any:
        """키가 key인 갖는 원소를 검색하여 값을 반환"""
        p = self.search_node(key)
        if p is not None:
            return p.value  # 검색 성공
        else:
            return None     # 검색 실패

    def add(self, key: Any, value: Any) -> bool:
        """키가 key이고 값이 value인 요소를 추가"""
        if self.search(key) is not None:
            return False             # 이미 등록된 키

        hash = self.hash_value(key)  # 추가하는 키의 해시값
        p = self.table[hash]         # 버킷을 주목
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)  # 재해시
            p = self.table[hash]
        return False                        # 해시 테이블이 가득 참

    def remove(self, key: Any) -> int:
        """키가 key인 갖는 요소를 삭제"""
        p = self.search_node(key)  # 버킷을 주목
        if p is None:
            return False           # 이 키는 등록되어 있지 않음
        p.set_status(Status.DELETED)
        return True

    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            print(f'{i:2} ', end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key} ({self.table[i].value})')
            elif self.table[i].stat == Status.EMPTY:
                print('-- 미등록 --')
            elif self.table[i] .stat == Status.DELETED:
                print('-- 삭제 완료 --')



from enum import Enum

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])

def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep = '  ', end='')
        n = int(input(': '))
        if 1 <=  n <= len(Menu):
            return Menu(n)

hash = OpenHash(13)  # 크기가 13인 해시 테이블 생성

while True:
    menu = select_menu()  # 메뉴 선택

    if menu == Menu.추가:  # 추가
        key = int(input('추가할 키를 입력하세요.: '))
        val = input('추가할 값을 입력하세요.: ')
        if not hash.add(key, val):
            print('추가를 실패했습니다!')

    elif menu == Menu.삭제:  # 삭제
        key = int(input('삭제할 키를 입력하세요.: '))
        if not hash.remove(key):
            print('삭제를 실패했습니다!')

    elif menu == Menu.검색:  # 검색
        key = int(input('검색할 키를 입력하세요.: '))
        t = hash.search(key)
        if t is not None:
            print(f'검색한 키를 갖는 값은 {t}입니다.')
        else:
            print('검색할 데이터가 없습니다.')

    elif menu == Menu.덤프:  # 덤프
        hash.dump()

    else:  # 종료
        break