class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        raman_dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        check = "I" 
        res = 0
        for i in s[::-1]:
            if raman_dic[i] < raman_dic[check]:
                res -= raman_dic[i]
                check = i
            else:
                res += raman_dic[i]
                check = i
        return res