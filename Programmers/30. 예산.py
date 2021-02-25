# 첫 번째 풀이 - sort() & Greedy
def solution(d, budget):
    d.sort()
    n = 0
    for dep in d:
        if dep <= budget:
            budget -= dep
            n +=1
    return n