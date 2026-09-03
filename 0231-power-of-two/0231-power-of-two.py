class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i=0
        while True:
            if 2**i==n:
                return True
                break
            elif 2**i>n:
                return False    
            else:
                i=i+1
                continue 

        