class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        compare = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in compare.values():
                stack.append(char)
            else:
                if not stack or compare[char] != stack.pop():
                    return False

        return len(stack) == 0