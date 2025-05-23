"""
# Time Complexity :
- O(log n), binary search is performed twice

# Space Complexity :
- O(1), no extra space used

# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def findRight():
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left_idx = findLeft()
        right_idx = findRight()

        # Check if the target is present
        if left_idx <= right_idx:
            return [left_idx, right_idx]
        else:
            return [-1, -1]
