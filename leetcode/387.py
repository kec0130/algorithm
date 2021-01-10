from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # 각 문자 수 집계
        count = Counter(s)
        # 1회 사용된 문자의 인덱스 반환
        for i in s:
            if count[i] == 1:
                return s.index(i)
        # 1회만 사용된 문자가 없으면 -1 반환
        return -1