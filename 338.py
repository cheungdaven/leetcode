class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = [0 for _ in xrange(0, n + 1)]
        for i in xrange(1, n + 1):
            count[i] += count[i & (i - 1 )] + 1
        return count