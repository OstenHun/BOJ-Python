"""
"문제 풀이 아이디어"
-> p일 중 l일 동안 캠핑장을 이용할 수 있고 v일 휴가를 나온다.
v일의 휴가 중 캠핑장의 p일로 나눈 몫을 l일로 곱해준다. 
이렇게 되면 v를 p로 나눈 나머지가 나타나는데, 이 값이 l 보다 크냐, 작냐, 같냐로 조건이 나뉜다.
나머지 값이 l보다 작다면 나머지를 v//p 와 더하여 최대 일 수를 나타내면 된다.
나머지 값이 l보다 크거나 같다면 그냥 l값을 출력해주면 된다. 크든 같든 최대로 사용할 수 있는 일 수가 l일이기 때문.
"""
cnt = 1
while True:
	day_cnt = 0
	day = 0

	l, p, v = map(int, input().split())
	if l == 0 & p == 0 & v == 0:
		break

	day_cnt += v // p
	v %= p
	day += day_cnt * l

	if v <= l:
		day += v
	else:
		day += l

	print('Case ' + str(cnt) + ': ' + str(day))
	cnt += 1
