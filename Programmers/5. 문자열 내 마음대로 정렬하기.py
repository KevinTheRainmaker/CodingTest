# First Code
def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n]+strings[i]
    strings.sort()
    
    for i in range(len(strings)):
        strings[i] = strings[i][1:]
        answer.append(strings[i])
        
    return answer

# Refactoring 1 (21.02.19)
def solution(strings, n):
    strings = [i[n]+i for i in strings]
    strings.sort()
    
    return [x[1:] for x in strings]