# 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율 구하기
c = int(input())

for _ in range(c):
    data = list(map(int, input().split()))
    n = data[0]
    scores = data[1:]
    avg = sum(scores) / n
    cnt = 0

    for score in scores:
        if score > avg:
            cnt += 1

    print(str("%.3f%%" % round(cnt / n * 100, 3)))
