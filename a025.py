class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """  
        if n <= 0: 
            return False
        else: 
            while n % 4 == 0: 
                n = n / 4 
            if n == 1: 
                res = True 
            else: 
                res = False 
        return res

