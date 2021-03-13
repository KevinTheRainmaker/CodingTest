def solution(arr):
    small = min(arr)
    answer = [i for i in arr if i != small]
    if len(answer) == 0:
        answer = [-1]
    return answer