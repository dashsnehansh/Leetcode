class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Edge case: numbers less than or equal to 0 are not ugly numbers
        if n <= 0:
            return False
            
        # Explicitly loop through the allowed prime factors 2, 3, and 5
        for factor in[2,3,5]:
            while n % factor == 0:
                n //= factor  # Divide n by the factor completely
                
        # If n drops all the way to 1, it is an ugly number
        return n == 1


