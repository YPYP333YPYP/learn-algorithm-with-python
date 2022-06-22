# 두 배열

from re import A
from typing import Sequence, MutableSequence

def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence) :
    """정렬을 마친 배열 a와 b를 병합하여 c에 저장"""
    pa, pb, pc = 0, 0, 0                 # 각 배열의 커서
    na, nb, nc = len(a), len(b), len(c)  # 각 배열의 원소수 

    while pa < na and pb < nb:  # pa와 pb를 비교하여 작은 값을 pc에 저장
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        else:
            c[pc] = b[pb]
            pb += 1
        pc += 1

    while pa < na:              # a에 남은 원소를 복사
        c[pc] = a[pa]
        pa += 1
        pc += 1

    while pb < nb:              # b에 남은 원소를 복사
        c[pc] = b[pb]
        pb += 1
        pc += 1

a1 = [1,3,5,7,9]
a2 = [0,2,4,6,8,10]
a3 = [None] * (len(a1) + len(a2))

merge_sorted_list(a1,a2,a3)
print(a1,a2,a3)

""" 해설 : 위 코드는 배열의 병합과정을 보여준다. 이미 정렬된 두 배열을 가지고 pa,pb,pc 변수는 0으로 초기화 해주고
    na,na,nc 변수는 배열의 크기만큼 설정해준다. 그 다음 두 원소의 크기를 비교하여 작은 값을 위 코드에서는 배열 c 에다가 저장한다
    예를 들어 a[pa] = 1 이고 b[pb] = 0 이다. 이럴 경우엔 더 작은 값인 0이 c[pc]에 들어갈 것이다. 그리고 pb +=1 을 해주고 pc += 1을 하게되면
    다음 비교는 a[pa] = 1 이고 b[pb] = 2 이다. 이럴 경우엔 더 작은 값인 1이 c[pc]에 들어갈 것이다. 이런 식으로 반복되며 배열 c에 값을 저장하다가
    두 배열의 크기는 다를 수 있으므로 가장 마지막 값들이 a,b 배열 안에 남아있을 수 있다. 남아 있는 원소들을 배열 c에 복사해주면 병합이 완료된다. """



def merge_sort(a: MutableSequence) :
    """병합 정렬"""

    def _merge_sort(a: MutableSequence, left: int, right: int) :
        """a[left] ~ a[right]를 재귀적으로 병합 정렬"""
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)            # 배열 앞부분을 병합 정렬
            _merge_sort(a, center + 1, right)       # 배열 뒷부분을 병합 정렬

            p = j = 0
            i = k = left

            while i <= center: # 배열 a의 앞부분을 buff 배열에 복사
                 buff[p] = a[i]
                 p += 1
                 i += 1

            while i <= right and j < p: # 배열 a의 뒷부분과 복사된 buff의 원소를 병합
                 if buff[j] <= a[i]:
                     a[k] = buff[j]
                     j += 1
                 else:
                     a[k] = a[i]
                     i += 1
                 k += 1

            while j < p:    # 남아 있는 buff의 원소들을 배열 a에 복사
                a[k] = buff[j]
                k += 1
                j += 1

    n = len(a)
    buff = [None] * n           # 작업용 배열을 생성
    _merge_sort(a, 0, n - 1)    # 배열 전체를 병합 정렬
    del buff                    # 작업용 배열을 소멸
    return a

x = [1,3,12,6,4,11,8,7,3,2,6,5]
print(merge_sort(x))



""" 해설 : 병합 정렬은 결국엔 배열을 두 그룹으로 나누고 정렬 시킨 후 병합하는 과정을 가진다.
    먼저 배열의 크기에 따라 두 그룹을 나누고 각각 정렬을 한다. 이는 재귀 함수로 표현할 수 있는데
    앞부분 정렬은 left(맨 왼쪽) ~ center(중간)의 범위를 가지고, 뒷 부분 정렬은 center(중간) + 1 ~ right(맨 오른쪽)의 범위를 가진다
    재귀 호출로 정렬된 두 그룹은 작업용 배열 buff를 통해서 병합 되는데 일단 앞부분 (a[left] ~ a[center])은 그대로 buff 배열의 앞 부분에 차례대로 복사된다.
    그 다음 배열의 뒷 부분 (a[center + 1] ~ a[right])과 buff로 복사한 배열의 앞부분을 병합하고 결과를 a에 저장한다.
    이후 배열 buff에 남아 있는 원소를 배열 a에 저장한다
     """