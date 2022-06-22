from re import A
from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:
    """힙 정렬"""

    def down_heap(a: MutableSequence, left: int, right: int) -> None:
        """a[left] ~ a[right]를 힙으로 만들기"""
        temp = a[left]      # 루트

        parent = left
        while parent < (right + 1) // 2:
            cl = parent * 2 + 1     # 왼쪽 자식
            cr = cl + 1             # 오른쪽 자식
            child = cr if cr <= right and a[cr] > a[cl] else cl  # 큰 값을 선택합니다.
            if temp >= a[child]:
                break
            a[parent] = a[child]
            parent = child
        a[parent] = temp

    n = len(a)

    for i in range((n - 1) // 2, -1, -1):   # a[i] ~ a[n-1]을 힙으로 만들기
        down_heap(a, i, n - 1)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]     # 최댓값인 a[0]과 마지막 원소 a[i]를 교환
        down_heap(a, 0, i - 1)      # a[0] ~ a[i-1]을 힙으로 만들기


    return a

x = [1,3,9,4,7,8,6]
print(heap_sort(x))


""" 해설 : 힙 정렬은 힙의 특성을 이용한 정렬이다. 여기서 힙의 특성은 힙은 부모 >= 자식인 부분 순서 트리를 가지고 있는데 여기서 부모 >= 자식 임을 이용한 정렬이다.
    쉽게 말하자면 힙 트리에서 최댓값인 루트를 배열의 맨 오른쪽에 저장한다. 그 후로 트리를 다시 힙 트리로 만드는데 이 과정을 거치면 새로운 최댓값을 가진 힙트리가 생성된다
    그러면 또 루트 값을 저장하는 식으로 정렬이 된다. 여기서 중요한 부분은 배열을 힙 트리로 만드는 과정이다. 이는 간단하게 이진 트리의 특성을 살리면 되는데
    트리의 최 하단의 오른쪽 부분이 가장 작은 값이 들어간다. 이 부분부터 부모 >= 자식 의 대소 관계를 만들어 주면 된다. 최 하단의 오른쪽이 관계가 만들어지면 최 하단의 왼쪽을 힙 관계로
    만들어주고 그런 식으로 올라가면서 결국에는 완성된 힙 트리의 모양을 가질 수 있다.  """
