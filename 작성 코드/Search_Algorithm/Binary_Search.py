from typing import Any, Sequence
import copy


def bin_search(a: Sequence, key:Any) ->int:
    pl = 0 # 배열의 시작 인덱스
    pr = len(a) - 1 # 배열의 마지막 인덱스

    while True:
        pc = (pl+pr) // 2 # 배열의 중간값 인덱스
        if a[pc] == key:
            return pc
        elif a[pc] < key: # 중간값과 key값의 크기 차이에 따라 범위를 새로 지정
            pl = pc + 1
        else : 
            pr = pc -1
        if pl > pr: # 결론적으로 pl은 1, pr은 0이 됨
            break
    return -1


if __name__ == '__main__':
    # 정렬된 배열임을 
    x_sort = [2,14,25,35,42,57,62]
    num = int(input('Key 값 : '))
    if bin_search(x_sort, num) >= 0:
         print(f'해당 숫자의 인덱스 번호는 x[{bin_search(x_sort, num)}] 입니다')
    else :
         print(f'해당 숫자는 없습니다')
    
