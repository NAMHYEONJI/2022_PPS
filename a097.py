class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        a, b = 0, len(numbers) - 1

        while a < b:
            sum = numbers[a] + numbers[b]
            if sum == target:
                return [a + 1, b + 1]
            if sum > target:
                a -= 1
            else:
                b += 1

        return None