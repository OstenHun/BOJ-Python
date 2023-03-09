"""
"문제 풀이 아이디어"
-> L의 이름을 가진 리스트 속에 동전 종류를 오름차순(입력 받은 순서대로)으로 삽입
N 종류의 동전 중 K 이하의 동전으로만 구성 가능하다
따라서, pop()을 통해 입력 받은 동전 종류 중 K값보다 큰 동전은 삭제
이후엔 '거스름돈' 예제에서 적용한 알고리즘을 이용해 K원 만드는데 필요한 동전 개수의 최솟값 구하기
"""

import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

L = []
for _ in range(N):
	L.append(int(sys.stdin.readline().rstrip()))
for i in range(N):
	if L[len(L) - 1] > K:
		L.pop()

# '거스름돈' 문제의 알고리즘 활용
count = 0
coin_types = sorted(L, reverse=True)
for coin in coin_types:
	count += K // coin
	K %= coin

print(count)

# 내 풀이
"""
result = 0
for i in range(1, len(L) - 1):
	cnt = 0
	cnt = K // L[len(L) - i]
	K -= cnt * L[len(L) - i]
	result += cnt
	if K == 0:
		break
print(result)
"""
