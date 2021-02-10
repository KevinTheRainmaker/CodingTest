def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i]+numbers[j])
            my_set = set(answer)
            my_answer = list(my_set)    # 파이썬의 set은 해시셋이기 때문에 정렬이 보장되지 않는다
            my_answer.sort()    # 따라서 sort()를 나중에 해줘야 함
    return my_answer