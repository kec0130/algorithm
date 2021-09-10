# (세 자리 수) × (세 자리 수) 곱셈 출력

a = int(input())
b = str(input())

x = a * int((b)[2])
y = a * int((b)[1])
z = a * int((b)[0])

print(x, y, z, sep='\n')
print(a * int(b))