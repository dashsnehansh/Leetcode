class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
       
        sign = -1 if x < 0 else 1
        x = abs(x)
        
      
        x_str = str(x)
        x_list = list(x_str)
        x_list.reverse()
        
        r = 0
        for i in range(len(x_list)):
            l = int(x_list[i])  
            r = r * 10 + l
        r = r * sign
        if r < -2**31 or r > 2**31 - 1:
            return 0
            
        return r

        