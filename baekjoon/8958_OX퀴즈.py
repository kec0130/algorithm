n = int(input())

# OX 퀴즈의 score를 계산
for i in range(n):
    ox = input()
    score = 0
    point = 0

    # 맞은 문제의 point는 그 문제까지 연속된 O의 개수
    for j in ox:
        if j == "O":
            point += 1
            score += point
        else:
            point = 0

    print(score)
