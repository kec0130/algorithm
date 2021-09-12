# 원래 수로 돌아올 때까지 연산을 반복하는 문제

# 1
n = str(input())
count = 0
n_list = [int(n)]

while True:
    if len(n) == 2:
        sum = int(n[0]) + int(n[1])
        n = n[1] + str(sum)[-1]
    else:
        n = n * 2
    
    count += 1
    n_list.append(n)

    if int(n) == n_list[0]:
        break

print(count)


# 2
n = int(input())
num = n
count = 0

while True:
    a = num // 10
    b = num % 10
    num = b * 10 + (a + b) % 10
    count += 1

    if num == n:
        break

print(count)