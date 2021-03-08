def solution1(x):
    div = 0
    for i in str(x):
        div += int(i)
    return x % div == 0


def solution2(x):
    return x% sum([int(i) for i in str(x)]) == 0

# 이왕 꼼수 쓸거면 더 확실히 써보자