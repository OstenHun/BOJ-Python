"""
"문제 풀이 아이디어"
-> 오름차순으로 정렬하게 되면 최소의 시간으로 돈을 뽑는다.; 'sort()' 이용해 풀이
"""
import sys

N = int(input())

L = list(map(int, sys.stdin.readline().rstrip().split()))
num = 0
Sum = 0
L.sort()
for i in range(N):
	num += L[i]
	Sum += num
	#Sum += L.pop() * (i + 1)
print(Sum)
