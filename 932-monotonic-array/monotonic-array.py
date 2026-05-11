class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isMonoInc = True
        isMonoDec = True
        n = len(nums)
        for i in range(1,n):
            if nums[i] < nums[i-1]:
                isMonoInc = False
            if nums[i] > nums[i-1]:
                isMonoDec = False

        return isMonoInc or isMonoDec