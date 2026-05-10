class Solution:
    def maxSubArray(self,nums:List[int])->int:
        currentSum = nums[0]
        ans = nums[0]
        n = len(nums)
        print(n)
        for i in range(1,n):
            if currentSum < 0:
                currentSum = 0
            currentSum = currentSum + nums[i]
            if ans < currentSum:
                ans = currentSum
        return ans