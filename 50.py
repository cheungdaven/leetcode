class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1

        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2 == 0:
            return self.myPow(x * x, n / 2)
        if n % 2 != 0:
            return self.myPow(x * x, n / 2) * x

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow