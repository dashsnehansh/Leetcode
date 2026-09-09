class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            digits = list(str(n))
            current_sum = 0
            for i in digits:
                current_sum += int(i) ** 2
                n = current_sum
        return n == 1

               