class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        y = str(num)
        
        
        while len(y) > 1:
            l = []
           
            for i in y:
                l.append(int(i))
            
            
            y = sum(l)
            y = str(y)
            
        
        return int(y)


        