from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:

    n = len(a)
    for i in range(n - 1):
        min = i  # 정렬 할 부분에서 가장 작은 원소의 인덱스
        for j in range(i + 1, n):
            if a[j] < a[min]: # 최솟값 비교
                min = j
        a[i], a[min] = a[min], a[i]  # 정렬 할 부분에서 맨 앞의 원소와 가장 작은 원소를 교환 
    return a


x = [1,3,9,4,7,8,6]
print(selection_sort(x))

""" 해설 : 선택 정렬은 원소 중 가장 작은 값을 정렬되지 않은 부분의 맨 앞 원소와 교환한다.
    교환 횟수는 n개의 데이터에 대해 n-1번이며, 처음 교환때 전체 원소 중 가장 작은 값이 a[min]으로 대입되며
    처음 a[i]는 i = 0 일때 임으로 가장 첫번째 인덱스에 값이 들어가고, min = i 식을 통해 정렬된 a[0] 번째 이후
    즉, i+1(a[1]) 값 부터 교환이 시작되며 정렬된 부분에서 교환이 일어나지 않도록 한다.  """