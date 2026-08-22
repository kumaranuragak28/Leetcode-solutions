class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paris = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in paris:
                if not stack or stack[-1] !=paris[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack)== 0
        