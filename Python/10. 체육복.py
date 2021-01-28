def solution(n, lost, reserve):
    answer =0
    overlap = []
    for r in reserve:
        for l in lost:
            if l == r:
                overlap.append(r)
    for ov in overlap:
        reserve.remove(ov)
        lost.remove(ov)

    for i in range(1, n+1):
        Lost = i in lost
        sThanks = i-1 in reserve
        bThanks = i+1 in reserve
        if Lost == False:
            answer+=1
        else:
            if sThanks == True:
                answer +=1
                reserve.remove(i-1)
            elif bThanks == True:
                answer +=1
                reserve.remove(i+1)
            else:
                continue
    return answer