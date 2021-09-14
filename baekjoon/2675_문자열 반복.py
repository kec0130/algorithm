# 각 문자를 주어진 횟수만큼 반복하여 출력하는 문제
t = int(input())
for _ in range(t):
    data = list(input().split())
    r = int(data[0])
    s = str(data[1])
    text = ""
    for i in s:
        text += i * r
    print(text)
