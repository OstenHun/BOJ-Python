"""
"문제 풀이 아이디어"
-> 00시 00분 00초 부터 N시 59분 59초까지 K가 포함 된 경우를 완전 탐색으로 카운트
"""
N, K = map(int, input().split())
Time = [0, 0, 0, 0, 0, 0]
cnt = 0


def one(i):
	if Time[i] == 10:
		Time[i] = 0
		Time[i - 1] += 1


def second(i):
	if Time[i] == 6:
		Time[i] = 0
		Time[i - 1] += 1


while True:
	if Time.count(K) != 0:
		cnt += 1
	Time[5] += 1

	one(5)
	second(4)
	one(3)
	second(2)
	one(1)

	if Time == [N // 10, N % 10 + 1, 0, 0, 0, 0]:
		break
print(cnt)
