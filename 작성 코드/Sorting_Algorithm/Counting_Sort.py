from typing import MutableSequence

def fsort(a: MutableSequence, max: int) :
    """도수 정렬(배열 원솟값은 0 이상 max 이하)"""
    n = len(a)           # 정렬할 배열 a
    f = [0] * (max + 1)  # 누적 도수 분포표 배열 f
    b = [0] * n          # 작업용 배열 b

    for i in range(n):              f[a[i]] += 1                     # [1단계]
    for i in range(1, max + 1):     f[i] += f[i - 1]                 # [2단계]
    for i in range(n - 1, -1, -1):  f[a[i]] -= 1; b[f[a[i]]] = a[i]  # [3단계]
    for i in range(n):              a[i] = b[i]                      # [4단계]

def counting_sort(a: MutableSequence) :
    """도수 정렬"""
    fsort(a, max(a))
    return a

x = [5,7,0,2,4,10,3,1,3]
print(counting_sort(x))


""" 해설 : 도수 정렬은 원소의 대소관계를 판단하지 않고 정렬하는 기법이다.
    이때 새로운 도수 분포표를 이용하게 되는데 과정을 4단계로 설명할 수 있다.
    <1단계>
    먼저 배열 a를 이용해서 key와 value를 가지는 배열 f가 만들어 지는데 
    과정은 배열 a의 value가 배열 f의 key가 되며 배열 f의 value는 +1 이 된다. 즉
    배열 a[2] = 5 라고 가정할때 f[5] +=1 이 되는 것이다. 이 과정을 반복하면 배열 f를 만들 수 있다. 
    <2단계> 
    배열 f를 가지고 도수분포표를 만들게 되는데 과정은 f[i] += f[i+1] 의 과정을 밟으면 된다.
    쉽게 말하면 바로 앞의 원솟값과 자신의 원솟값을 더해서 새로운 자신의 원솟값을 설정하는 것 이다.
    <3단계>
    여기선 작업용 배열 b가 등장하는데 이는 배열 a와 도수분포표를 대조하여 정렬을 완료한 배열을 만드는 것이다.
    이 과정을 쉽게 말하면 일단 a[n-1] 부터 시작되는데 a[n-1]의 value가 배열 f의 key인 값을 찾는다 그러면 value값을 얻을 수 있는데
    이때 배열 f의 value - 1 이 배열 b의 key가 되고 배열 b의 value는 배열 f의 key값이 된다. 
    이 과정을 반복하다가 배열 a에서 같은 value값을 가지는 경우가 있는데 이 경우 배열 f에서 배열 b로 가는 과정에서 배열 f의 value를 -1 시켜 
    배열 b의 key 값에 매칭 한다. 
    <4단계>
    이렇게 만들어진 배열 b를 배열 a에 복사하면 된다."""
