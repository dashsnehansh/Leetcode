class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = set()
        nums.sort()
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                    
        return [list(p) for p in s]
