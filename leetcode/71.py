class Solution:
    def simplifyPath(self, path: str) -> str:
        # slash 단위로 디렉토리명 나누기
        dir = path.split("/")
        stack = []
        # 디렉토리명 하나씩 확인하며
        for i in dir:
            # 현재 디렉토리(.) or 빈 문자열이면 넘어감
            if i == "." or i == "":
                continue
            # 상위 디렉토리(..)이고 스택이 비지 않았으면 마지막 원소 꺼내기
            elif i == "..":
                if stack:
                    stack.pop()
            # 그 외 디렉토리명은 스택에 추가
            else:
                stack.append(i)
        # slash 붙여서 연결
        return "/" + "/".join(stack)