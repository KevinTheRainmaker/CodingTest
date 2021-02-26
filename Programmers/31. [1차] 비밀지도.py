# 첫 번째 풀이 - No Refactoring
def solution(n, arr1, arr2):
    an = [[format(a,'b').zfill(n),format(b,'b').zfill(n)] for a,b in zip(arr1, arr2)]
    swer = []
    sad = ''
    for t in an:
        for i in range(n):
            if t[0][i] == '1' or t[1][i] == '1':
                swer.append('#')
            else:
                swer.append(' ')
    answer = [a for a in swer]
    for k in answer:
        sad += k

    return [sad[n*k:n*(k+1)] for k in range(n)]