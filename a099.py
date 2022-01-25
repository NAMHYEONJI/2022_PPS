class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        li = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                li.append(i)
            else:
                if not li:
                    return False
                if i == ")" :
                    if li.pop() != '(':
                        return False
                elif i == "}":
                    if li.pop() != '{':
                        return False
                elif i == "]":
                    if li.pop() != '[':
                        return False
        if li:
            return False
        return True