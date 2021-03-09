import math

def solution(n):
    if math.sqrt(n) == round(math.sqrt(n)):
        return math.pow(math.sqrt(n)+1,2)
    return -1

# 제곱근이 정수인지 판별하는 부분 아이디어가 여러 가지 나올 수 있다.



def othersSol(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0: # 제곱근을 1로 나눈 나머지가 0이면 정수
        return (sqrt + 1) ** 2
    return -1 # return 'no'라고 되어있던데 이유가 뭘까

