# 첫 번째 풀이 - 효율성에서 탈락
def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i)
    
    return participant[0]

# 두 번째 풀이 - 성공
def solution(p,c):
    p.sort()
    c.sort()
    for par, com in zip(p, c) :
        if par != com :
            return par
    return p[-1]

# 다른 사람의 풀이 - collection 라이브러리의 Count 메서드를 적절히 사용
import collections

def solution(p, c):
    answer = collections.Counter(p) - collections.Counter(c)
    return list(answer.keys())[0]