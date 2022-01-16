class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while True:
            num = str(num)
            if len(num) == 1:
                return num
            sum = 0
            for n in num:
                sum += int(n)
            num = sum