class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        l1=0
        l2=1
        l3=0
        if n>1:
              for i in range(n-1):
                    l3=l1+l2
                    l1=l2
                    l2=l3
              return l3    
        if n==0:
            return 0
        if n==1:
            return 1        
