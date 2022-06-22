from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence) -> None:
    """이진 삽입 정렬"""
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0      # 검색 범위의 맨 앞 원소 인덱스
        pr = i - 1  # 검색 범위의 맨 끝 원소 인덱스

        while True:
            pc = (pl + pr) // 2  # 검색 범위의 중앙 원소 인덱스
            if a[pc] == key:     # 검색 성공
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break
    
        pd = pc + 1 if pl <= pr else pr + 1  # 삽입할 위치의 인덱스

        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key
    
    return a


x = [1,3,9,4,7,8,6]
print(binary_insertion_sort(x))


""" 해설 : 선택 정렬의 특성 상 선택한 원소를 정렬된 원소들 사이에서 삽입 하는 과정은 배열의 크기가 커질 수록 비교,
    교환 비용이 커진다. 그러므로 이진 검색의 특성을 이용하여 이미 정렬된 원소들은 비교 대상에서 제외하여 이러한 비용을 줄일 수 있다.
    """