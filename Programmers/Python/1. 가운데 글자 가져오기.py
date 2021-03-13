# First Code
def solution(s):
    answer = ''
    length = len(s)
    if length%2 == 0:
        answer = s[length//2-1]+s[length//2]
    else:
        answer = s[length//2]
    return answer

# Refactoring 1 (21.02.19)
def solution(s):
    return s[(len(s)-1)//2:len(s)//2+1] 
    # 슬라이싱을 이용하여 s의 글자수가 홀수개인지 짝수개인지에 관계없이 하나의 코드로 완성시켰다