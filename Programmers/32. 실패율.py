# First Code - RunTime Error
import operator

def solution(N, stages):
    num = len(stages)
    if (N+1) in stages:
        stages.remove((N+1))
    a = {stage:stages.count(stage) for stage in range(1,N+1)}
    peoples = [num]
    people = 0
    for i in range(N):
        people += a[i+1]
        peoples.append(num-people)
    if num > len(stages):
        peoples = peoples[:len(stages)-num]
    failure = dict()
    for i in range(N):
        fail = a[i+1]/peoples[i]
        failure[i+1] = fail
    almost = sorted(failure.items(), key=operator.itemgetter(1), reverse=True)
    answer = [thing[0] for thing in almost]
    return answer

# Refactoring - peoples의 값이 0이 되어 나누지 못하는 경우 고려하여 list comprehension 내 조건문 삽입
import operator

def solution(N, stages):
    num = len(stages)
    a = {stage+1:stages.count(stage+1) for stage in range(N)}
    peoples = [num]
    people = 0
    for i in range(N):
        people += a[i+1]
        peoples.append(num-people)
    failure = {i+1:a[i+1]/peoples[i] if peoples[i] != 0 else a[i+1] for i in range(N)}
    almost = sorted(failure.items(), key=operator.itemgetter(1), reverse=True)
    return [thing[0] for thing in almost]