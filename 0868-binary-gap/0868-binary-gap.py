class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=[]
        while True:
            p= n%2    
            l.append(p)
            if n==1:
                break
            n= n//2
        l.reverse()    
        maxi=-1
        smax=-1
        count=0
        ans=0    
        for i in range (len(l)):
            if l[i]==1:
                    smax=maxi
                    maxi=i
                    count+=1
                    ans= max(ans, maxi-smax)
        if count>1:
            return ans
        else:
            return 0                