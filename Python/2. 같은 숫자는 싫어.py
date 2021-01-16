def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i-1]==arr[i]:
            answer
        else:
            answer.append(arr[i])
    return answer

arr = []

while(1):
    Input = input('Enter: ')
    if Input != '-1':
        arr.append(Input)
    else:
        break

print(solution(arr))