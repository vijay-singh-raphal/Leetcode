class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        first = 0
        last = len(nums)-1
        ans = [1]*len(nums)
        i = len(nums)-1
        while i >= 0:
            if (nums[first]**2) > (nums[last]**2):
                ans[i] = nums[first]**2
                first = first+ 1
            else:
                ans[i] = nums[last]**2
                last = last - 1
            i = i - 1
        return ans