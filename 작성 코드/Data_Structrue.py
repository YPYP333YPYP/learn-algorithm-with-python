# 배열 원소의 최댓값 구하기

from re import X
from typing import Any,Sequence,MutableSequence

def max_of(a:Sequence) -> Any:
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

# 배열 원소를 역순으로 정렬

def reverse_array(a:MutableSequence) -> Any:
    n = len(a)
    for i in range(n // 2):
        a[i], a[n-i-1] = a[n-i-1],a[i]
    return a


# 기수 변환하기 (n) 진수 구하기

def card_conv(x:int, r:int) -> str: # x= 정수, r= 변환할 진수
    d = ''
    dchar= '0123456789ABCDEF'

    while x > 0:
        d += dchar[x%r]
        x //= r
    
    return d[::-1]

# 1부터 정수까지의 소수 구하기

def prime_number(num:int) -> Sequence:
    ptr = 0
    prime = [None] * 10000

    prime[ptr] = 2
    ptr += 1

    for n in range(3,num+1,2):
        for i in range(1, ptr):
            if n % prime[i] == 0:
                break
        else:
            prime[ptr] = n
            ptr +=1
    prime = list(filter(None,prime))
    return prime


if __name__ == '__main__':
    x = [11,22,33,44,55,66,77,88,99]

    print(max_of(x)) 
    print(reverse_array(x))
    print(card_conv(29,2)) 
    print(prime_number(10000))