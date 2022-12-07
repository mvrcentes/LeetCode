class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        print(nums)
        if len(nums) % 2 == 0:
            print(nums[len(nums) // 2])
            print(nums[(len(nums) // 2) + 1])
            return float(nums[len(nums) // 2] + nums[(len(nums) // 2) - 1] ) / 2
        else:
            return float(nums[len(nums) // 2])
s = Solution()
# print(s.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))
print(s.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))
# print(s.findMedianSortedArrays(nums1=[1, 3], nums2=[2, 7]))