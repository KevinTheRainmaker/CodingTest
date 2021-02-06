def solution(a, b):
    answer = 0
    if a>b:
        a, b = b, a
    
    if a==b:
        answer = a
    else:
        answer = sum(range(a,b+1))
    return answer