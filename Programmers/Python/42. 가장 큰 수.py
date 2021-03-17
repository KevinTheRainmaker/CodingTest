import operator

def solution(numbers):
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

# Not Done