# 스택: 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 다섯 가지이다.
 # push X: 정수 X를 스택에 넣는 연산이다.
 # pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
 # size: 스택에 들어있는 정수의 개수를 출력한다.
 # empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
 # top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

# 입력 
 # 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 
 # 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 
 # 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 
 # 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력 
 # 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

# 예제 입력          # 예제 출력
 # 14                # 2
 # push 1            # 2
 # push 2            # 0
 # top               # 2
 # size              # 1
 # empty             # -1
 # pop               # 0
 # pop               # 1
 # pop               # -1
 # size              # 0
 # empty             # 3
 # pop
 # push 3
 # empty
 # top

''''''
# 스택 기능 구현 - push와 pop은 내장함수로 이용 가능하나, 빈 리스트에서 pop을 이용하는 경우를 생각하여 직접 구현해준다
class Stack:
    def __init__(self):
        self.len = 0
        self.list = []
        
    def push(self, item):
        self.list.append(item)
        self.len += 1

    def pop(self):
        if self.size() == 0:
            return -1
        data = self.list[self.len -1]
        del self.list[self.len -1]
        self.len -= 1
        return data

    def size(self):
        return self.len

    def empty(self):
        return 1 if self.len == 0 else 0

    def top(self):
        return self.list[-1] if self.size() != 0 else -1

# 코드
n = int(input())
stack = Stack()
answer = []
for _ in range(n):
    cmd = input().split()
    i = cmd[0]
    if i == 'push':
        stack.push(cmd[1])
    elif i == 'pop':
        answer.append(stack.pop())
    elif i == 'size':
        answer.append(stack.size())
    elif i == 'empty':
        answer.append(stack.empty())
    else:
        answer.append(stack.top())

for a in answer:
    print(a)