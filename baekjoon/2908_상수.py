# 숫자를 뒤집어서 대소 비교하는 문제
a, b = map(str, input().split())
print(max(int(a[::-1]), int(b[::-1])))

# 문자열 뒤집는 방법
# a[::-1]
# ''.join(reversed(a))
