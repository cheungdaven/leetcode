class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parenmap = {"}": "{", ")": "(", "]": "["}

        for p in s:
            if p not in parenmap:
                stack.append(p)
            elif not stack or parenmap[p] != stack.pop():
                return False
        return not stack