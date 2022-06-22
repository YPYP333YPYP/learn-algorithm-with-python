def kmp_match(txt: str, pat: str) -> int:
    """KMP법에 의한 문자열 검색"""
    pt = 1  # txt를 따라가는 커서
    pp = 0  # pat를 따라가는 커서
    skip = [0] * (len(pat) + 1)  # 건너뛰기 표

    # 건너뛰기 표 만들기
    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

    # 검색하기
    pt = pp = 0
    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        elif pp == 0:
            pt += 1
        else:
            pp = skip[pp]

    return pt - pp if pp == len(pat) else -1



txt1 = 'ABWSGAETFASDFFASDWDASWRE'
pat1 = 'SWRE'

print(kmp_match(txt1,pat1))


""" 해설 : kmp 방법은 브루트 포스 방법을 약간 보완한 방법이라고 말할 수 있는데, 예를 들어 텍스트가 'ABABC' 라고하고 패턴이 'ABC' 라고 가정하면
    브루트 포스 방법은 처음 'AB' 부분에서 일치하더라도 'C'부분이 일치 하지 않기 때문에 다음 인덱스로 넘어가 검색을 하는데 kmp 방법은 'AB' 부분 까지는 맞았다는 것을
    기억해서 해당 시작 부분을 'AB'로 설정하고 그 다음 문자열부터 검색을 할 수 있게 된다.
    이 방법을 사용하기 위해 '건너뛰기 표(skip table)'를 사용하는데 만드는 방법은 패턴을 서로 나란히 놓고 서로 겹치는 부분이 있을 경우 해당 부분 만큼 숫자로 더해주어 표를 완성하는 것이다.
    자세하게 설명하면 
    A B A B C 가 패턴이라고 했을때 처음 패턴과 패턴을 서로 매칭하게 된다. 정지해 있는 패턴을 pat1, 움직이는 패턴을 pat2라고 했을 때 pat2가 움직이고 0번째 인덱스부터 pat1에 대하여 매칭을 시작한다
    이때 겹치는 부분만큼 +n을 해주면 되는 것이다. 이런식으로 진행하면 건너뛰기 표가 만들어진다.
    이로 인해서 패턴으로 텍스트를 검색할 때 만약 패턴에서의 AB가 텍스트에도 있으면 +2 만큼 건너뛰기 하고 다음 문자열부터 매칭할 수가 있게 된다. """