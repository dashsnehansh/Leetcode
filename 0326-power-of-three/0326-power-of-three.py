class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i=0
        while True:
            if n==3**i:
                return True
                break
            elif 3**i>n:   
                return False    
            else:
                i=i+1    