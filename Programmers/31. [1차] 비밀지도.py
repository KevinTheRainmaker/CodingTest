# 첫 번째 풀이 - No Refactoring
def solution1(n, arr1, arr2):
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


# Refactoring - 압축율 max
def solution2(n, arr1, arr2):
    # list comprehenshion에 []가 한 번만 있을 경우 앞의 for가 이중 for문에서 바깥쪽 for문
    return [''.join([' ' if int(t[0][i])+int(t[1][i]) == 0 else '#' for t in [[format(a,'b').zfill(n),format(b,'b').zfill(n)]\
     for a,b in zip(arr1, arr2)] for i in range(n)])[n*k:n*(k+1)] for k in range(n)]


# Refactoring - 의 적당한 줄타기 + 변수명 조정
def solution3(n, arr1, arr2):
    binary = [[format(a,'b').zfill(n),format(b,'b').zfill(n)] for a,b in zip(arr1, arr2)]
    shop = [' ' if int(t[0][i])+int(t[1][i]) == 0 else '#' for t in binary for i in range(n)]
    answer = [''.join(shop)[n*k:n*(k+1)] for k in range(n)]
    return answer


# Refactoring - 가독성 up
def solution4(n, arr1, arr2):
    binary = [[format(a,'b').zfill(n),format(b,'b').zfill(n)] for a,b in zip(arr1, arr2)]
    shop = []
    for t in binary:
        for i in range(n):
            if t[0][i] == '1' or t[1][i] == '1':
                shop.append('#')
            else:
                shop.append(' ')

    return [''.join(shop)[n*k:n*(k+1)] for k in range(n)]