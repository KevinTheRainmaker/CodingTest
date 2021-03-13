# First Code
def solution(s):
    s = s.lower()
    p=0
    y=0
    for i in range(len(s)):
        if s[i] == 'p':
            p+=1
        elif s[i] == 'y':
            y+=1

    return p==y

# Refactoring 1 (21.02.19)
def solution(s):
    s = s.lower()
    p, y = (0, 0)
    for i in s:
        if i == 'p':
            p+=1
        elif i == 'y':
            y+=1

    return p==y

# Refactoring 2 (21.02.19)
def solution(s):
    return s.lower().count('p') == s.lower().count('y')
    # 문자열 내 특정 문자를 찾아 수를 자동으로 집계해주는 count()함수를 사용