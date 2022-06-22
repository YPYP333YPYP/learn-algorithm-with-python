# 버블 정렬

from typing import MutableSequence

def bubble_sort(a: MutableSequence):
    n = len(a)
    count = 0
    for i in range(n-1):
        for j in range(n-1,i,-1):
            count +=1
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
               
                
    return a,count            

x = [1,3,9,4,7,8,6]
print(bubble_sort(x))

""" 해설 : 버블정렬은 n개의 데이터가 있다고 가정할 시 n-1 번 교환을 수행하여 가장 작은 값을 배열의 첫 번째 원소에 오도록 한다.
    또한 배열 상으로 n-1(배열의 마지막 데이터) 번째 데이터부터 시작해서 0번째 인덱스까지 데이터 값의 비교를 통해서 교환을 하며
    가장 작은 값이 0번째 인덱스 값에 오면 2번째로 작은 값을 1번째 인덱스에 오게하며 교환을 진행한다.
    이렇게 가장 작은 값을 왼쪽으로 교환해 나가는 과정을 '패스' 라고 하며 버블 정렬의 패스는 n-1번 이다. 

    비교 횟수 : 21번
"""

# 알고리즘 개선 1

def bubble_sort_imp1(a: MutableSequence):
    n = len(a)
    count = 0
    for i in range(n-1):
        exchng = 0
        for j in range(n-1,i,-1):
            count +=1
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                exchng +=1
        if exchng == 0:
            break 
    return a, count      

x = [1,3,9,4,7,8,6]
print(bubble_sort_imp1(x))


""" 해설 : 패스에서 교환을 진행하다가 교환이 더 이상 진행되지 않는 패스 또한 존재할 것 이다. 이는 정렬 되었다는 것을 의미한다.
    일반화 해서 말하면 '교환이 한번도 일어나지 않은 패스 뒤의 패스 또한 교환이 일어나지 않는다' 라고 말할 수 있다
    exchng 변수를 통해서 교환 할때마다 +1 을 하여 교환이 한번도 일어나지 않은 즉, exchng가 0인 경우엔 정렬을 종료한다.
    
    비교 횟수 : 20번
    """

# 알고리즘 개선 2

def bubble_sort_imp2(a: MutableSequence):
    n = len(a)
    count = 0
    k = 0
    
    while k < n-1:
    
        last = n-1
        for j in range(n-1,k,-1):
            count +=1
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
               
        k = last
    return a, count      

x = [1,3,9,4,7,8,6]
print(bubble_sort_imp2(x))

""" 해설 : 패스에서 교환을 진행하다가 특정한 원소 이후로 교환이 되지 않는다면 그 원소보다 앞쪽에 있는 원소는 이미 정렬을 마친 것이다.
    즉 마지막 교환이 이뤄진 부분에서의 두 원소중 오른쪽 인덱스 (코드 상에서는 a[j]의 값)을 last 에다가 대입한다
    이러면 범위가 n-1 ~ k 까지로 축소 되고 마지막 교환이 일어나는 지점이 a[k] 와 a[k+1]이 된다. 
    
    비교 횟수 : 12번
"""

# 셰아커 정렬


def shaker_sort(a: MutableSequence) :
    left = 0
    right = len(a) - 1
    last = right
    count = 0 
    while left < right:
        for j in range(right, left, -1):
            count +=1
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                last = j
        left = last

        for j in range(left, right):
            count +=1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                last = j
        right = last
    
    return a,count

x = [1,3,9,4,7,8,6]
print(shaker_sort(x))

""" 해설 : 셰이커 정렬은 홀수 패스에서는 n-1 에서 마지막 배열까지 <- 방향으로 교환을 이어나가고
    짝수 패수에서는 정렬된 원소 이후 원소부터 마지막 원소까지 -> 방향으로 교환을 이어 나간다.
    이렇게 스캔방향을 거꾸로 번갈아 가며 바꾸면 적은 비교 횟수로 정렬 할 수 있다.
    
    비교 횟수 : 11번 """
