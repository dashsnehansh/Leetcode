class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()
        s = s[::-1]
        i = 0
        
        while i < len(s):
            if s[i] == " ":
                return i
            else:
                i += 1
        return i
