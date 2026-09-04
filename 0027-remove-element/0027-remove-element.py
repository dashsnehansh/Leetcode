class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        x = len(nums)
        a = 0  # 'a' will keep track of the index for valid numbers
        
        for i in range(len(nums)):
            # Check the original value FIRST before changing anything
            if nums[i] != val:
                nums[a] = nums[i]  # Move the valid number to index 'a'
                a += 1             # Move 'a' forward
                
        # At this point, 'a' is exactly equal to the new length (y)
        y = a 
        z = x - y
        
        # Append the underscores to 'nums' directly instead of an undefined 'l'
        for i in range(z):
            nums.append("_")
            
        return y
  