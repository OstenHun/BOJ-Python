"""
"문제 풀이 아이디어"
-> collections 라이브러리 속 deque을 이용해서 풀 수 있다고 생각했다.
('문제 제목부터 덱 인점, pop(), append(), popleft(), appendleft()를 이용하면 좋은 상황 제시' 따라서 deque을 연습해보는 문제라고 판단)
"""

# 내 풀이
from collections import deque
import sys

data = deque()

N = int(input())

for _ in range(N):
	n = list(map(str, sys.stdin.readline().rstrip().split()))

	# 정수를 덱의 앞에 넣음
	if n[0] == 'push_front':
		data.appendleft(int(n[1]))

	# 정수를 덱의 뒤에 넣음
	elif n[0] == 'push_back':
		data.append(int(n[1]))

	# 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력 만약, 덱에 정수가 없다면 -1을 출력
	elif n[0] == 'pop_front':
		if data == deque():
			print(-1)
		else:
			l_num = data.popleft()
			print(l_num)

	# 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력 이하 동문
	elif n[0] == 'pop_back':
		if data == deque():
			print(-1)
		else:
			R_num = data.pop()
			print(R_num)

	# 덱에 들어있는 정수의 개수를 출력
	elif n[0] == 'size':
		print(len(data))

	# 덱이 비어있으면 1, 아니면 0 출력
	elif n[0] == 'empty':
		if data == deque():
			print(1)
		else:
			print(0)

	# 덱의 가장 앞에 있는 정수 출력. 만약 덱에 정수 없는 경우 -1 출력
	elif n[0] == 'front':
		if data == deque():
			print(-1)
		else:
			print(data[0])

	# 덱의 가장 뒤에 있는 정수 출력. 이하 동문
	elif n[0] == 'back':
		if data == deque():
			print(-1)
		else:
			print(data[len(data) - 1])
