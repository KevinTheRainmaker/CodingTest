# def solution(arr, divisor):
#     answer = []
#     for i in range(len(arr)):
#         if arr[i]%divisor==0:
#             answer.append(arr[i])
#         else:
#             answer
#     if len(answer)==0:
#         answer.append(-1)
#     answer.sort()
#     return answer

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

