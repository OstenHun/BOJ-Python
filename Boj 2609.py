import math

a, b = map(int, input().split())

print(math.gcd(a, b))  # 최대공약수 출력
print(math.lcm(a, b))  # 최소공배수 출력
