"""
"문제 풀이 아이디어"
-> '거스름돈'문제와 동일한 알고리즘으로 풀이
"""
M = int(input())

coin_types = [500, 100, 50, 10, 5, 1]

cnt = 0
change = 1000 - M
for coin in coin_types:
	cnt += change // coin
	change %= coin
print(cnt)