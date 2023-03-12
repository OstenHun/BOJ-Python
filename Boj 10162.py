"""
"문제 풀이 아이디어"
-> '거스름 돈' 문제를 약간 변형한 문제 동일한 알고리즘이 사용된다.
"""
T = int(input())
cnt = [0, 0, 0]
Time = [300, 60, 10]

# '거스름 돈' 알고리즘 활용
for i in range(3):
	cnt[i] = T // Time[i]
	T %= Time[i]

if T != 0:
	print(-1)
else:
	print(cnt[0], cnt[1], cnt[2])
