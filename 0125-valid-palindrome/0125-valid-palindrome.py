class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c=""
        for i in s.lower():
            if i.isalnum():
                c+=i   
        if c[::-1]==c:
            return True
        else:
            return False    



