class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        while True:
            length = len(s)
            if i == length:
                break
            if s[i] == "#" and i == 0:
                s = s.replace(s[i], "", 1)
            elif s[i] == "#":
                s = s.replace(s[i-1]+s[i], "")
                i -= 1
            else:
                i += 1

        i = 0
        while True:
            length = len(t)
            if i == length:
                break
            if t[i] == "#" and i == 0:
                t = t.replace(t[i], "", 1)
            elif t[i] == "#":
                t = t.replace(t[i-1]+t[i], "")
                i -= 1
            else:
                i += 1

                
        if s == t:
            return True
        return False