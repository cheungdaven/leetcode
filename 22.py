class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.list = []
        self._gen(0, 0, n, "")
        return self.list

    def _gen(self, left, right, n, res):
        if left == n and right == n:
            self.list.append(res)
            return

        if left < n:
            self._gen(left + 1, right, n, res + "(")
        if right < left and right < n:
            self._gen(left, right + 1, n, res + ")")