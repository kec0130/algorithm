n = int(input())
score = list(map(int, input().split()))
sum = 0
# 점수/최댓값*100의 평균
for i in score:
    sum += i / max(score) * 100
print(sum / n)

