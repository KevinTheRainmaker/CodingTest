def solution(s):
    answer = ''
    rs = sorted(s)
    rs.reverse()
    for i in range(len(rs)):
        answer += rs[i]
    return answer