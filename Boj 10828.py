"""
"문제풀이 아이디어"
-> deque 기능을 활용해 풀이
"""
from collections import deque
import sys

N = int(input())

data = deque()

for _ in range(N):
	s = list(map(str, sys.stdin.readline().rstrip().split()))
	if s[0] == 'push':
		data.append(int(s[1]))
	elif s[0] == 'pop':
		if data == deque():
			print(-1)
		else:
			Top_num = data.pop()
			print(Top_num)
	elif s[0] == 'size':
		print(len(data))
	elif s[0] == 'empty':
		if data == deque():
			print(1)
		else:
			print(0)
	elif s[0] == 'top':
		if data == deque():
			print(-1)
		else:
			print(data[len(data) - 1])
