def solution(s):
    p = 0
    y = 0

    for i in range(len(s)):
        if s[i] == "p" or s[i] == "P":
            p += 1
        elif s[i] == "y" or s[i] == "Y":
            y += 1

    return p == y

# def solution(s):
#     answer = True
#     s = s.lower()
#     p=0
#     y=0
#     for i in range(len(s)):
#         if s[i] == 'p':
#             p+=1
#         elif s[i] == 'y':
#             y+=1

#     return p==y
