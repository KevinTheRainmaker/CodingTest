# 첫 번째 솔루션
def solution(n):
    triple = []
    answer = 0
    while n > 3:
        triple.append(n%3)
        n = n // 3
    if n == 3:
        triple.append(0)
        triple.append(1)
    else:
        triple.append(n)
    for i in range(len(triple)):
        answer += triple[i]*pow(3,len(triple)-(i+1))
    return answer


# 두 번째 수정된 솔루션
def solution(n):
    triple = []
    answer = 0
    while n > 0:
        triple.append(n%3)
        n = n // 3
    # if n == 3:
    #     triple.append(0)
    #     triple.append(1)
    # else:
    #     triple.append(n)
    for i in range(len(triple)):
        answer += triple[i]*pow(3,len(triple)-(i+1))
    return answer