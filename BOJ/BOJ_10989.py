# 수 정렬하기 3: N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
 # 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 
 # 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 
 # 이 수는 10,000보다 작거나 같은 자연수이다.

# 출력
 # 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력         # 예제 출력
 # 10               # 1
 # 5                # 1
 # 2                # 2
 # 3                # 2
 # 1                # 3
 # 4                # 3
 # 2                # 4
 # 3                # 5
 # 5                # 5
 # 1                # 7
 # 7

''''''
# 기존 정렬 문제와 달리 중복값이 있을 수 있다.

# 2751번 풀이 - 메모리 초과
import sys
n = int(sys.stdin.readline())
N = sorted([int(sys.stdin.readline()) for _ in range(n)])
print(*N, sep='\n')


# 내 풀이1: 배열 N을 저장하는 부분을 삭제 - 소요되는 메모리와 시간을 약간씩 줄이는 것을 성공하였으나 여전히 메모리 초과
import sys
n = int(sys.stdin.readline())
print(*sorted([int(sys.stdin.readline()) for _ in range(n)]), sep='\n')


# 내 풀이2: 새로운 해석 - 중복값을 하나의 공간에 저장 후 출력
import sys
n = int(sys.stdin.readline())
arr = [0]*10001 # 10,000보다 작거나 같다

for i in range(n):
    arr[int(sys.stdin.readline())] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)
            
# 성공 (메모리: 29284 KB. 시간: 9124 ms) 
# 소요시간이 많이 늘어났다. 과연 시간을 7배 가량 늘리면서 메모리를 줄일 이유가 있는가 의문이 들었다. 