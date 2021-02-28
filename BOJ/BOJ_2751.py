# 수 정렬하기2: N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
 # 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다.  -> 2750번에 비해 범위가 더 넓어짐
 # 둘째 줄부터 N개의 줄에는 숫자가 주어진다. 
 # 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 
 # 수는 중복되지 않는다.

# 출력
 # 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력           # 예제 출력
 # 5                  # 1
 # 5                  # 2
 # 4                  # 3
 # 3                  # 4
 # 2                  # 5
 # 1

''''''
# 2750번 코드 - 시간초과
n = int(input())
N = sorted([int(input()) for _ in range(n)])  
for a in N:
    print(a)


# 내 풀이1: 정렬과 출력을 하나의 프린트문에서 실행 - 여전히 시간초과 & 가독성 안 좋음
n = int(input())
print(*sorted([int(input()) for _ in range(n)]), sep = '\n')


# 내 풀이2: int형태로 받지않아도 sorted는 예상과 같은 순서로 뱉어낸다 - 역시 시간초과
n = int(input())
N = sorted([input() for _ in range(n)])
print('\n'.join(N))
# -라고 생각했으나 이 경우 12가 2보다 앞에 정렬된다.

# print(*sorted(['12', '3']),sep='\n')
# >> 12
# >> 3


# 내 풀이3: import sys
import sys
n = int(sys.stdin.readline())
N = sorted([int(sys.stdin.readline()) for _ in range(n)])
print(*N, sep='\n')
# 성공 (메모리: 83956 KB, 시간: 1372 ms)

# input과 달리 sys.stdin.readline은 file object로 취급되어 사용자의 입력만을 받는 buffer를 만들고 그로부터 값을 읽어들인다.
# sys.stdin.readline()은 사용자의 입력은 물론 개행문자도 입력 받을 수 있으며, 한 번에 읽어들일 문자의 수를 정하는 것이 가능하다.
# 대량의 입력을 받을 경우 input()과 sys.stdin.readline()의 속도 차이는 무시할 수 없는 수준이다.