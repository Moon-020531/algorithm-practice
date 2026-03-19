# enquene: 뒤에 데이터 추가
# deque: 앞에 데이터를 꺼냄

from collections import deque

queue = deque()
queue.append('A')  # enqueue A -> deque(['A'])
queue.append('B')  # enqueue B -> deque(['A', 'B'])
queue.append('C')  # enqueue C -> deque(['A', 'B', 'C'])
print(queue.popleft())  # -> A
print(queue.popleft())  # -> B