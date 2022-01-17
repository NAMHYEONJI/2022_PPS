class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left, right+1):
            check = True
            num_str = str(num)
            for n in num_str:
                if int(n) == 0:
                    check = False
                    break
                elif num % int(n) != 0:
                    check = False
                    break
            if check :
                res.append(num)
        return res