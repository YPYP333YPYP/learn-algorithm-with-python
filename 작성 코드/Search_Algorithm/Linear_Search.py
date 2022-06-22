# 선형 검색 알고리즘

from typing import Any, Sequence
import copy

def seq_search(a: Sequence, key: Any) -> int:
    i = 0

    while True:
        if i ==len(a): # key값에 맞지 않는 값들은 넘어가고
            return -1

        if a[i] == key: # key값이 일치하는 인덱스 번호를 반환 한다.
            return i
        i += 1

# 보초법을 추가한 선형 검색 알고리즘

def seq_search_sen(seq:Sequence, key:Any) -> int:
    a = copy.deepcopy(seq) # seq를 깊은 복사
    a.append(key) # 배열에 보초 key 추가
   

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
  
    if i == len(seq): # 보초법으로 인한 발견이면 -1, key값을 찾은 발견이면 해당 인덱스 번호를 반환
        return -1
    else :
        return i 


if __name__ == '__main__':
    x = [5,4,2,6,1,2,7,3]
    num1 = int(input('Key 값 : '))
    if seq_search(x, num1) >= 0 :
        print(f'해당 숫자의 인덱스 번호는 x[{seq_search(x, num1)}] 입니다')
    else :
        print(f'해당 숫자는 없습니다')

    # 보초법 사용 시
    num2 = int(input('Key 값 : '))
    if seq_search_sen(x, num2) >= 0:
         print(f'해당 숫자의 인덱스 번호는 x[{seq_search_sen(x, num2)}] 입니다')
    else :
         print(f'해당 숫자는 없습니다')
    

    