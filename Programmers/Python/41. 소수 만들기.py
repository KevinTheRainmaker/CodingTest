from itertools import combinations

def isPrime(num):
    if num == 1:
        return -1
    if num %2 == 0:
        return -1
    for i in [(k*2)-1 for k in range(2,num//2)]:
        if num % i == 0:
            return -1
    return 0
    
def solution(nums):
    answer = 0
    renums = [sum(i) for i in combinations(nums, 3)]
    for i in renums:
        if isPrime(i) == 0:
            answer += 1
    return answer


# Refactoring - isPrime의 리턴값을 0과 1로하여 계산을 간소화
from itertools import combinations

def isPrime(num):
    if num == 1:
        return 0
    if num %2 == 0:
        return 0
    for i in [(k*2)-1 for k in range(2,num//2)]:
        if num % i == 0:
            return 0
    return 1
    
def solution(nums):
    return sum([isPrime(sum(k)) for k in combinations(nums, 3)])