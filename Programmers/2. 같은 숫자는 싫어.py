# First Code
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i-1]==arr[i]:
            answer
        else:
            answer.append(arr[i])
    return answer
    
# Refactoring 1 (21.02.19)
def solution(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]: continue # answer 리스트의 가장 마지막 값이 arr의 i번째 값을 원소로 갖는 리스트와 같은가?
        # 같으면 아래 append를 실행시키지 않음(continue)
        # 여기서 핵심은 슬라이싱! 
        # 빈 리스트에 대하여 answer[-1]을 써주면 IndexError가 발생하지만, 
        # 슬라이싱을 이용하면 빈 리스트에 대해서도 정상적으로 작동한다.
        answer.append(i)
    return answer