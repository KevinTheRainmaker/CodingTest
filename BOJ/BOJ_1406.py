# 에디터

import sys 
from collections import deque 
class Editor: 
    def __init__(self, input_text): 
        self.left_deque = deque(input_text) 
        self.right_deque = deque() # 커서를 왼쪽으로 한칸 옮김 
    
    def move_cursor_left(self): 
        if self.left_deque: 
            self.right_deque.appendleft(self.left_deque.pop()) # 커서를 오른쪽으로 한칸 옮김 
    
    def move_cursor_right(self): 
        if self.right_deque: 
            self.left_deque.append(self.right_deque.popleft()) # 커서 왼쪽에 있는 문자를 삭제함 
    
    def delete_left_character(self): 
        if self.left_deque: 
            self.left_deque.pop() # 문자를 커서 왼쪽에 추가함 
            
    def add_character_to_left(self, character2add): 
        self.left_deque.append(character2add) 
        
        
editor = Editor(sys.stdin.readline().strip()) 

N = int(sys.stdin.readline().strip()) 
while N: 
    command = sys.stdin.readline().strip() 
    if command[0] == 'L': 
        editor.move_cursor_left() 
    elif command[0] == 'D': 
        editor.move_cursor_right() 
    elif command[0] == 'B': 
        editor.delete_left_character() 
    else: 
        editor.add_character_to_left(command[2]) 
    N -= 1 

print(''.join(editor.left_deque) + ''.join(editor.right_deque))