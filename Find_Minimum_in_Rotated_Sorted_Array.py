"""
# Time Complexity :
- O(log n), binary search approach

# Space Complexity :
- O(1), no extra space used

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
