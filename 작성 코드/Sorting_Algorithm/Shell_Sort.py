from typing import MutableSequence

def shell_sort(a: MutableSequence) :
   
    n = len(a)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 2

    return a

x = [1,3,9,4,7,8,6]
print(shell_sort(x))


""" 해설 : 쉘 정렬은 삽입 정렬의 단점(삽입할 위치가 너무 멀면 이동횟수가 많아짐)을 보안한 것으로 원소들을 그룹화 시켜서 그룹 별로 정렬을 수행한다.
    쉘 정렬은 변수 h가 등장하는데 이는 그룹화 시키기 위한 변수이다. 예를 들어 배열의 크기가 8이라면 h의 값은 4로 설정 된다. 즉 4개의 그룹을 만들어서
    4번의 정렬이 이뤄지는 것이다. 이런 식으로 h의 값은 4 - > 2 -> 1로 변화하며 총 7번의 정렬이 이뤄진다.
    정렬 과정의 코드를 보면 처음 정렬의 경우 h = 4 이면 i = 4가 된다. 이러면 j = 0이 되는데 이때 a[j+h]와 a[j]의 관계는 h칸 만큼 떨어진 그룹이 형성되는 것이다
    인덱스를 통해 정렬되는 그룹들을 보면 (0,4), (1,5), (2,6), (3,7) 번째 원소들이 그룹이 되어 정렬된다.
    """

# 쉘 정렬의 개선

def shell_sort(a: MutableSequence):
    """셸 정렬(h * 3 + 1의 수열 사용)"""
    n = len(a)
    h = 1

    while h < n // 9:
        h = h * 3 + 1

    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 3
    return a

x = [1,3,9,4,7,8,6]
print(shell_sort(x))

""" 해설 : 쉘 정렬의 단점은 h 값에 따라 그룹화를 시켜도 그룹화의 장점을 못살리는 경우가 존재하는데 이는 h의 값이 서로 배수가 되지 않도록 해야한다.
    이때의 h값의 패턴을 일반화하면 h = 3h + 1 이라는 일반식이 만들어 진다. 단, h의 초깃값이 지나치게 크면 효과가 없기 때문에 n을 9로 나누었을때 그 몫을
    넘지 않도록 해야한다. 결론적으로 그룹화 시키는 과정에서 h의 값을 3h + 1로 정해 설정함으로 그룹화의 효율을 늘린 알고리즘을 만들 수 있다."""
