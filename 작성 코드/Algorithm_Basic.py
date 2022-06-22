# 세 정수의 최댓값 구하기

from re import I


def max3(n1,n2,n3):
    maximum = n1
    if n2 > maximum : maximum = n2
    if n3 > maximum : maximum = n3
    return maximum

print(max3(3,2,1))


# 세 정수의 중앙값 구하기

def med3(n1, n2, n3):
    if n1 >= n2 :
        if n2 >= n3 : return n2
        elif n1 <= n3 : return n1
        else : return n3
    
    elif n1 > n3 : return n1

    elif n2 > n3 : return n3

    else : return n2

print(med3(1,3,5))


# 1부터 n까지 정수의 합 구하기

def sum_int(num):
    sum = 0
    i = 1

    while i <= num:
        sum += i  
        i += 1

    return sum

print(sum_int(5)) 


# 두 정수 사이의 연속하는 정수의 합 구하기

def sum_two_int(n1,n2):
    if n1 > n2: n1,n2 = n2, n1
    sum = 0
    for i in range(n1, n2+1):
        sum += i
    return sum

print(sum_two_int(4,9))

# 반복 과정에서 조건 판단하기 (*를 n개 출력하되 w개마다 줄바꿈)

def star_print(n,w):

    for i in range(n):
        print('*', end='')
        if i % w == w-1: print('')

    if n % w: print('')


# 직사각형 넓이로 변의 길이 구하기

def rectangle_area(area):

    for i in range(1, area+1):
        if i * i > area : break
        if area % i : continue
        print(f'{i} x {area // i}')

print(rectangle_area(64))

# 다중 루프 (구구단)

def gugudan():
    print('-' * 27)
    for i in range(1,10):
        for j in range(1,10):
            
            print(f'{i*j:3}', end='')
        print()
    print('-' * 27)

gugudan()

# 직각 이등변 삼각형 출력하기

def right_isosceles_triangle(num):
    for i in range(num):
        for j in range(i+1):
            print('*', end='')
        print()

right_isosceles_triangle(5)