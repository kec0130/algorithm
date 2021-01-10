class Solution:
    def reformatNumber(self, number: str) -> str:
        # 공백과 하이픈 제거
        num = number.replace(" ", "").replace("-", "")
        # 변수 초기값 설정
        answer = ""
        len_left = len(num)
        idx = 0
        # 숫자가 4개 남을 때까지 3개씩 이어 붙이 작업 반복
        while len_left > 4:
            answer += num[idx:idx+3] + "-"
            len_left -= 3
            idx += 3
        # 2개 or 3개 남으면 나머지 모두 붙이기
        if len_left in [2, 3]:
            answer += num[idx:]
        # 4개 남으면 2개씩 이어 붙이기
        else:
            answer += num[idx:idx+2] + "-" + num[idx+2:]
        return answer