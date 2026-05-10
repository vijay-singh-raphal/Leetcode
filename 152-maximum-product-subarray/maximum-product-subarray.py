class Solution:
    def maxProduct(self,nums:List[int])->int:
        maxPro = nums[0]
        minPro = nums[0]
        ans = nums[0]
        n = len(nums)
        for i in range(1,n):
            if nums[i]>=0:
                maxPro = max(nums[i],maxPro * nums[i])
                minPro = min(nums[i],minPro * nums[i])
            else:
                temp = maxPro
                maxPro = max(nums[i],minPro * nums[i])
                minPro = min(nums[i],temp * nums[i])
            ans = max(ans,maxPro)
        return ans