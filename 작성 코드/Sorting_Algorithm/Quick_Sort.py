# 재귀적 퀵 정렬

from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 퀵 정렬"""
    pl = left                   # 왼쪽 커서
    pr = right                  # 오른쪽 커서
    x = a[(left + right) // 2]  # 피벗(가운데 요소)

    while pl <= pr:    
        while a[pl] < x: pl += 1 # 왼쪽 그룹 스캔
        while a[pr] > x: pr -= 1 # 오른쪽 그룹 스캔
        if pl <= pr: # # 스캔된 값끼리의 교환
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(a, left, pr) # 재귀적 호출
    if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)
    return a

x = [5,8,4,2,6,1,3,9,7]
print(quick_sort(x))


""" 해설 : 퀵 정렬은 피벗(pivot)을 이용하여 두 그룹을 생성하고 이 과정을 반복해 정렬해 나가는 정렬 방법이다.
    배열에서 가장 왼쪽 값을 pl = left, 가장 오른쪽 값을 pr = right, 그리고 그 중간값(피벗)을 x라고 정해놓고
    피벗을 기준으로 왼쪽 그룹은 a[pl] >= x가 성립하는 원소를 찾을 때까지 오른쪽 방향으로 스캔하고
    피벗을 기준으로 오른쪽 그룹은 a[pr] <= x가 성립하는 원소를 찾을 때까지 왼쪽 방향으로 스캔한다.
    그러면 왼쪽 그룹은 피벗보다 큰 값을, 오른쪽 그룹은 피벗보다 작은 값을 갖게 되는데 이 두 원소를 교환한다
    이런식으로 반복하다보면 왼쪽은 피벗보다 작은 그룹, 오른쪽은 피벗보다 큰 그룹이 만들어 진다. 
    이것을 배열의 범위로 살피면 피벗 이하인 그룹 : a[0] ~ a[pl-1], 피벗 이상인 그룹 : a[pr+1] ~ a[n-1]이며 
    pl > pr + 1일때 한해서만 피벗과 일치하는 그룹 : a[pr + 1] ~ a[pl - 1] 이 만들어진다.
    이렇게 생성된 두 그룹을 가지고 또 두 그룹으로 만들면서 교환과 정렬을 반복하면 되는데 이때 재귀적 호출을 이용할 수 있다.
    즉, 왼쪽 그룹은 left(a[0]) < pr 인 경우에 = pr이 a[0]이 될때까지 = 왼쪽 그룹의 원소가 하나가 될 때 까지 함수를 재귀적으로 호출하고
    오른쪽 그룹은 pl < right(a[n-1]) 인 경우에 = pl이 a[n-1]이 될때까지 = 오른쪽 그룹의 원소가 하나가 될 때 가지 함수를 재귀적으로 호출한다
     """


# 비재귀적 퀵 정렬

from stack_copy import Stack  


def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a [right]를 퀵 정렬(비재귀 버전)"""
    range = Stack(right - left + 1)  # 스택 생성

    range.push((left, right))

    while not range.is_empty():
        pl, pr = left, right = range.pop()  # 왼쪽, 오른쪽 커서를 꺼냄
        x = a[(left + right) // 2]          # 피벗(중앙 요소)

        while pl <= pr:
            while a[pl] < x: pl += 1
            while a[pr] > x: pr -= 1
            if pl <= pr:                        
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr: range.push((left, pr))    # 왼쪽 그룹의 커서를 저장
        if pl < right: range.push((pl, right))  # 오른쪽 그룹의 커서를 저장

def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)
    return a

x = [5,8,4,2,6,1,3,9,7]
print(quick_sort(x))


""" 해설 : 재귀함수는 마찬가지로 스택을 이용하여 비재귀적인 호출로 바꿀 수 있는데 
    먼저 원소의 크기가 right(a[n-1]) - left(a[0]) - 1인 스택을 생성하고 
    left, right 값을 스택에 푸시한다. 스택이 비어 있지 않은 동안 작업을 반복하며 전에 했던 방식대로 left = pl, right = pr값을 대입해 그룹을 만들어주고
    만들어진 그룹을 스택에 푸시하는데 예를 들어 배열의 크기가 9인 배열이 있다 가정하면 그룹은 a[0] ~ a[4], a[5]~a[8]로 나눌 수 있다.
    이때 스택에는 (0,4)가 먼저 푸시되고 (5,8)이 나중에 푸시 되며 (5,8)은 또 다시 (5,6), (7,8)로 그룹화 된다 (7,8)은 그룹화 시키면 원소가 한개짜리 그룹이 되기 때문에
    스택에서 팝 되며 그 다음 (5,6)을 수행하고 이 과정을 반복해서 나중에 (0,1)을 수행하면 해당 반복문이 종료된다. """


# 시간 복잡도의 피벗, 원소의 크기의 비용을 최소화한 퀵 정렬 모델

def sort3(a: MutableSequence, idx1: int, idx2: int, idx3: int):
    """a[idx1], a[idx2], a[idx3]을 오름차순으로 정렬하고 가운데 값의 인덱스를 반환"""
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    if a[idx3] < a[idx2]: a[idx3], a[idx2] = a[idx2], a[idx3]
    if a[idx2] < a[idx1]: a[idx2], a[idx1] = a[idx1], a[idx2]
    return idx2

def insertion_sort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 단순 삽입 정렬"""
    for i in range(left + 1, right + 1):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 퀵 정렬"""
    if right - left < 9:            # 원소 수가 9개 미만이면 단순 삽입 정렬을 호출
        insertion_sort(a, left, right)
    else:                           # 원소 수가 9개 이상이면 퀵 정렬을 수행
        pl = left                   # 왼쪽 커서
        pr = right                  # 오른쪽 커서
        m = sort3(a, pl, (pl + pr) // 2, pr)
        x = a[m]

        a[m], a[pr - 1] = a[pr - 1], a[m]
        pl += 1
        pr -= 2
        while pl <= pr:
            while a[pl] < x: pl += 1
            while a[pr] > x: pr -= 1
            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr: qsort(a, left, pr)
        if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)
    return a

x = [5,8,4,2,6,1,3,9,7]
print(quick_sort(x))



""" 해설 : 먼저 원소의 수가 9개 미만인 경우 단순 삽입 정렬로 전환한다. 그 다음 sort3은 피벗 선택을 조정하여 실행효율에 영향을 미치는데,
    일단 배열에서 left(맨 왼쪽 값), right(맨 오른쪽 값), 가운데 원소를 정렬한다
    그 다음에 정렬된 가운데 원소와 right 바로 왼쪽 원소 즉 a[right-1]의 원소를 교환한다. 
    이렇게 되면 왼쪽 커서(pl) 위치는 left + 1 이 되고, 오른쪽 커서(pr) 위치는 right -2 가 된다. 
    그 후에 퀵 정렬을 수행하면 된다."""

