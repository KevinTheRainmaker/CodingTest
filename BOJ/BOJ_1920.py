# 수 찾기: N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력 
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 
# 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 
# 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 
# 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 
# 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

# 예제 입력         # 예제 출력
 # 5                 # 1
 # 4 1 5 2 3         # 1
 # 5                 # 0
 # 1 3 7 9 5         # 0
                     # 1

''''''
# 내 풀이: list comprehesion 이용
N = int(input())
Narr = set(map(int, input().split()))
M = int(input())
Marr = list(map(int, input().split()))
for ans in [int(a in Narr) for a in Marr]:
    print(ans)
# 성공! (메모리: 48280 KB, 시간: 208 ms)

''''''
# 다른 풀이1: Binary Search
from sys import stdin, stdout
n = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
M = map(int, stdin.readline().split())

def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)

for l in M:
    start = 0
    end = len(N)-1
    print(binary(l,N,start,end))
# 메모리: 41888 KB, 시간: 796 ms

''''''
# 다른 풀이2: set 자료형 이용 - 내 풀이와 유사
from sys import stdin, stdout
n = stdin.readline()
N = set(stdin.readline().split())
m = stdin.readline()
M = stdin.readline().split()

for l in M:
    stdout.write('1\n') if l in N else stdout.write('0\n')
# 메모리: 47988 KB, 시간: 172 ms - 가장 우수
# 이유(예상): 내 풀이의 마지막 출력문 부분을 비교하는 부분과 합침

''''''
# 수정된 내 풀이
N = int(input())
Narr = set(map(int, input().split()))
M = int(input())
Marr = list(map(int, input().split()))
for l in Marr:
    print('1') if l in Narr else print('0')
# 시간 개선
# 메모리: 48280 KB (유지)
# 시간: 188 ms (20 ms 단축)