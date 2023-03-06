"""
"문제풀이 아이디어"
-> deque 기능을 활용해 풀이
"""
from collections import deque
import sys

N = int(input())

data = deque()

for _ in range(N):
	n = list(map(str, sys.stdin.readline().rstrip().split()))

	if n[0] == 'push':
		data.append(int(n[1]))
	elif n[0] == 'pop':
		if data == deque():
			print(-1)
		else:
			L_num = data.popleft()
			print(L_num)
	elif n[0] == 'size':
		print(len(data))
	elif n[0] == 'empty':
		if data == deque():
			print(1)
		else:
			print(0)
	elif n[0] == 'front':
		if data == deque():
			print(-1)
		else:
			print(data[0])
	elif n[0] == 'back':
		if data == deque():
			print(-1)
		else:
			print(data[len(data) - 1])
