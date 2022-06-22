# 팩토리얼 함수
def factorial(n: int) -> int:
 
    if n > 0:
        return n * factorial(n - 1) # n이 0이 될때까지 자기 자신 함수를 호출
    else:
        return 1

if __name__ == '__main__':

    print(f'값 : {factorial(5)}')