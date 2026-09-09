class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for i in nums2:
            nums1.append(i)
        nums1.sort( )    
        if len(nums1)%2!=0:
            s=(len(nums1)+1)/2
            return nums1[s-1]
        else:
            s=len(nums1)/2
            t=(len(nums1)/2)+1
            y=(nums1[s-1]+nums1[t-1])/2.0
            return y   