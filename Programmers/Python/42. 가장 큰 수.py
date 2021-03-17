# 첫번째 풀이 - 수를 4자리로 늘려 dict에 저장 후 정렬하여 붙이기
import operator

def solution1(numbers):
    an = dict()
    for number in numbers:
        if len(str(number)) == 1:
            an[number] = (str(number)*4)
        if len(str(number)) == 2:
            an[number] = (str(number)*2)
        if len(str(number)) == 3:
            an[number] = (str(number)+number[0])

    answers = sorted(an.items(), key=operator.itemgetter(1), reverse = True)

    return "".join([str(answer[0]) for answer in answers])
# 런타임 에러 발생


# 두번째 풀이 - 단순히 늘리고 잘라 위 과정 반복
# map과 lambda를 사용했다
def solution2(numbers):
    numbers = list(map(str,numbers))
    answer = [(number,(str(number)*4)[:4]) for number in numbers]
    s = sorted(answer, key = lambda answer:answer[1], reverse = True)
    return "".join([num[0] for num in s])
# 테스트 케이스 11 실패



# 세번째 풀이 - 테스트 케이스 11번을 0으로 return하기 위해 int > str 변환 과정 추가
def solution3(numbers):
    numbers = list(map(str,numbers))
    answer = [(number,(str(number)*4)[:4]) for number in numbers]
    s = sorted(answer, key = lambda answer:answer[1], reverse = True)
    return str(int("".join([num[0] for num in s])))
# 성공 (+8)