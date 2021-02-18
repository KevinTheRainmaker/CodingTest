def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i)
    
    return participant[0]

# 답은 모두 정상적으로 도출해내지만 효율성이 걸림돌이 되었다. 이 부분에 대해서 다시 공부해서 통과할 수 있도록 
