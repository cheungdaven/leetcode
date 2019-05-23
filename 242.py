class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False

        alph_dict_s = {}
        alph_dict_t = {}
        for i in s:
            alph_dict_s[i] = alph_dict_s.get(i, 0) + 1
        for i in t:
            alph_dict_t[i] = alph_dict_t.get(i, 0) + 1
        if alph_dict_s == alph_dict_t:
            return True
        return False