class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        y, m, d = date.split('-')
        y, m, d = int(y), int(m), int(d)
        m_dic = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        res = d
        for i in range(1, m):
            if (i == 2 and (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0))):
                res += 29
            else:
                res += m_dic[i]
        return res