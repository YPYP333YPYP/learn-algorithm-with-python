def bm_match(txt: str, pat: str) -> int:
    """보이어 무어법에 의한 문자열 검색"""
    skip = [None] * 256  # 건너뛰기 표

    # 건너뛰기 표 만들기
    for pt in range(256): # 1번의 경우 
        skip[pt] = len(pat)
    for pt in range(len(pat)): # 2번의 경우
        skip[ord(pat[pt])] = len(pat) - pt - 1 # ord 함수는 문자를 정수로 반환

    # 검색하기
    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp \
              else len(pat) - pp

    return -1

txt1 = 'ABWSGAETFASDFFASDWDASWRE'
pat1 = 'SWRE'

print(bm_match(txt1,pat1))


""" 해설 : 보이어 무어 방법의 가장 핵심은 패턴의 마지막 문자열을 먼저 비교한다는 것 이다. 만약 마지막 문자열이 일치하지 않으면 어차피 텍스트에서 패턴이 없다는 것을 의미하기 때문이다
    그러면 패턴을 패턴의 크기만큼 텍스트에서 스킵해서 매칭을 진행할 수 있다. 또한 매칭을 진행하다가 전체 패턴이 일치하지 않아도 패턴의 일부분이 일치하는 경우 그 부분부터 매칭을 시작할 수 있다.
    이를 위해서는 보이어 무어 방법에서도 표가 필요한데 표를 만드는 방법은 크게 2가지 경우로 구성된다.
    1. 패턴에 포함되지 않는 문자를 만난 경우, 2. 패턴에 포함되는 문자를 만난 경우 이다, 이때 패턴의 문자열의 길이가 n이라고 가정할때 
    1번의 경우 패턴의 크기만큼 패턴을 이동시켜 주면 되기 때문에 n 만큼 이동하면 된다
    2번의 경우 마지막에 나오는 위치의 인덱스가 k라 할때 이동량은 n - k - 1이 된다. 또한 같은 문자가 패턴 안에서 중복해서 존재하지 않으면 패턴의 맨 끝 문자의 이동량은 n이 된다"""