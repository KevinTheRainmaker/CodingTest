def solution(s):
    answer = ''
    length = len(s)
    if length%2 == 0:
        answer = s[length//2-1]+s[length//2]
    else:
        answer = s[length//2]
    return answer

s = input()
print(solution(s))