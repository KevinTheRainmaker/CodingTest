from fractions import Fraction as fr

def solution(n,m):
    a=[]
    f=fr(n,m) # n/m의 분수표현
    if n>m: # 가분수이면
        a.append(n/f.numerator) # numerator = 분자
        a.append(m*f.numerator)
    else:
        a.append(n/f.numerator)
        a.append(n*f.denominator) # denominator = 분모
    return a