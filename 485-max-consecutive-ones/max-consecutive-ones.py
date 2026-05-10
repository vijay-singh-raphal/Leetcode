class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                count = count+1
            if ans < count:
                ans = count
            if nums[i] == 0:
                count = 0
        return ans
        