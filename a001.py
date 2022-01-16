class Solution:
    def findContentChildren(self, g, s):
        g = sorted(g)
        s = sorted(s)
        
        idx = 0
        res = 0
        for i in range(len(g)):
            for j in range(idx, len(s)):
                if g[i] <= s[j] :
                    idx = j + 1
                    res += 1
                    break
        return res