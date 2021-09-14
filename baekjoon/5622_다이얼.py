# 주어진 문자에 대응하는 번호로 전화를 걸기 위해 필요한 최소 시간 구하기
word = input().lower()
alphabet = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

time = 0
for i in word:
    for j in alphabet:
        if i in j:
            time += alphabet.index(j) + 3
print(time)
