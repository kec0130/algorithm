class Solution:
    def arrangeWords(self, text: str) -> str:
        # 공백 단위로 쪼개고 단어 길이 순으로 정렬
        words = sorted(text.split(), key=len)
        # 띄어쓰기로 연결하고 첫 글자를 대문자로 변경
        return " ".join(words).capitalize()