# First Code
def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i]%divisor==0:
            answer.append(arr[i])
        else:
            answer
    if len(answer)==0:
        answer.append(-1)
    answer.sort()
    return answer

# Refactoring 1 (21.02.19)
def solution(arr, divisor):
    answer = []
    for i in arr: # 반복문에 대한 개념이 부족한 상태였기에 했던 실수(?)
        if i%divisor==0:
            answer.append(i)
        else:
            answer
    if len(answer)==0:
        answer.append(-1)
    answer.sort()
    return answer

# Refactoring 2 (21.02.19)
def solution(arr, divisor): 
    return sorted([n for n in arr if n%divisor == 0]) or [-1] # list comprehension 이용
    # arr의 원소 n이 divisor에 의해 나눠 떨어지면 리스트에 삽입
    # 그렇지 않으면(or 앞이 전부 거짓이면) -1 삽입
    # 만들어진 리스트 내 원소를 정렬하여 'str 형태의 원소'를 가진 '리스트'로 반환
    # ex - sorted([1,3,2,7,5]) >> ["1","2","3","5","7"]