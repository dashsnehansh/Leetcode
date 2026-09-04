class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i=0
        while True:
            if i*i==num:
                return True
            elif i*i>num:
                return False
            else:
                i=i+1
