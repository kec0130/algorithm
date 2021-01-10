class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 문자열을 공백 단위로 쪼개기
        words = s.split()
        # 단어가 없으면 0 return
        if len(words) == 0:
            return 0
        # 마지막 단어의 길이 return
        else:
            answer = len(words[-1])
        return answer