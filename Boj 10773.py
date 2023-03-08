"""
"문제 풀이 아이디어"
-> 스택 사용하여 풀이.
"""
stack = []

N = int(input())

for _ in range(N):
	nm = int(input())
	if nm == 0:
		stack.pop()
	else:
		stack.append(nm)

Sum = sum(stack)
print(Sum)
