## 한 단어에서 각 알파벳이 처음 등장하는 위치를 찾는 문제

# 1. find를 사용하는 방법
word = input()
alphabet = list(range(ord("a"), ord("z") + 1))  # 아스키코드 숫자 범위

for x in alphabet:
    print(word.find(chr(x)))


# 2. 배열을 만들어놓고 한 자리씩 대조하는 방법
S = input()
check = [-1] * 26

for i in range(len(S)):
    if check[ord(S[i]) - ord("a")] != -1:
        continue
    else:
        check[ord(S[i]) - ord("a")] = i

for i in range(26):
    print(check[i], end=" ")
