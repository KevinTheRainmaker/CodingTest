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

arr = []

while(1):
    Input = int(input('Enter: '))
    if Input != -1:
        arr.append(Input)
    else:
        break

divisor = int(input("Divide for what?: "))
print(solution(arr, divisor))