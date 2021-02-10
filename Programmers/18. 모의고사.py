def solution(answers):
    supo_1 = [1,2,3,4,5]
    supo_2 = [2,1,2,3,2,4,2,5]
    supo_3 = [3,3,1,1,2,2,4,4,5,5]
    s_1 = 0
    s_2 = 0
    s_3 = 0
    top = []
    for i in range(len(answers)):
        if supo_1[i%5] == answers[i]:
            s_1 += 1
        if supo_2[i%8] == answers[i]:
            s_2 += 1
        if supo_3[i%10] == answers[i]:
            s_3 += 1
    if s_1 == s_2:
        if s_1>s_3:
            top.append(1)
            top.append(2)
        elif s_1==s_3:
            top.append(1)
            top.append(2)
            top.append(3)
        else:
            top.append(3)
    elif s_1 == s_3:
        if s_1>s_2:
            top.append(1)
            top.append(3)
        else:
            top.append(2)
    elif s_2 == s_3:
        if s_2>s_1:
            top.append(2)
            top.append(3)
        else:
            top.append(1)
    else:
        if s_1 == max(s_1,s_2,s_3):
            top.append(1)
        if s_2 == max(s_1,s_2,s_3):
            top.append(2)
        if s_3 == max(s_1,s_2,s_3):
            top.append(3)
            
    return top


# enumerate 등 이용하여 좀더 깔끔한 코딩방법을 생각해 볼 것
