class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i=0
        while True:
              if n==4**i:
                return True
                break
              elif n<4**i: 
                return False
              else:
                i+=1  
              