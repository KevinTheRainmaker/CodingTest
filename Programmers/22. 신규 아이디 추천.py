def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def solution(new_id):
    delete = []
    # 1단계
    new_id = new_id.lower()
    # print(1, new_id)

    # 2단계
    delete = []
    for i in range(len(new_id)):
        if ord(new_id[i]) < 97 or ord(new_id[i]) > 122:
            if isNumber(new_id[i]) != True:
                if new_id[i] != '-' and new_id[i] != '_' and new_id[i] != '.':
                    delete.append(new_id[i])
                    
    for k in range(len(delete)):
        new_id = new_id.replace(delete[k],'')
    # print(2, new_id)

    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    # print(3, new_id)

    # 4단계
    if len(new_id) > 1:
        if new_id[0] == '.':
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    else:
        if new_id[0] == '.':
            new_id =''
    # print(4, new_id)

    # 5단계
    if len(new_id) == 0 :
        new_id += 'a'
    # print(5, new_id)

    # 6단계
    if len(new_id) >= 16 :
        new_id = new_id[:15] 
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    # print(6, new_id)

    # 7단계
    while len(new_id) <= 2 :
        new_id += new_id[-1]
    # print(7, new_id)

    return new_id