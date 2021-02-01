# n=int(input())
# d=[0]*(n+1)
# for i in range(n) :
#     print(d)
#     if(d[i+1]<d[i]) :
#         d[i+1]=d[i]
#     print(d)
#     t, p=map(int, input().split())
#     if(i+t<=n) :
#         if(d[i+t]<d[i]+p) :
#             d[i+t]=d[i]+p
#     print(d)
# print(max(d))

n = int(input())
work = []
pmax = [0] * n

for _ in range(n):
    work.append(list(map(int, input().split())))
    # print(work)
for i in range(n-1, -1, -1): #뒤에서부터 앞으로 이동
    day = work[i][0]
    pay = work[i][1]
    
    if day > n - i: #남은 기간보다 상담일이 길 경우
        if i != n-1:  
            pmax[i] = pmax[i+1]
        continue

    if i == n-1: #마지막 날 의뢰가 하루만에 끝나는 의뢰일 경우
        pmax[i] = pay
    elif i + day == n: #마지막 날에 딱 맞춰 의뢰를 완수할 수 있는 경우
        pmax[i] = max(pay, pmax[i+1])
    else:
        pmax[i] = max(pay + pmax[i + day], pmax[i+1])
        
print(pmax[0])
