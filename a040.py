class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        half_len = int(len(s)/2)
        a = s[:half_len]
        b = s[half_len:]
        a_cnt = 0
        b_cnt = 0
        for i in range(half_len):
            if a[i] in "aeiouAEIOU":
                a_cnt += 1
            if b[i] in "aeiouAEIOU":
                b_cnt += 1
        if a_cnt == b_cnt:
            return True
        return False