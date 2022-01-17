import math
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sqrt = math.sqrt(num)
        if sqrt * 10 % 10 == 0:
            return True
        return False