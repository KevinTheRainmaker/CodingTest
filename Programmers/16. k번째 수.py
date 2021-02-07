def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        if commands[i][0]==commands[i][1]:
            unit = array[commands[i][0]-1]
            answer.append(unit)
        else:
            unit = array[commands[i][0]-1:commands[i][1]]
            unit.sort()
            answer.append(unit[commands[i][2]-1])
    return answer