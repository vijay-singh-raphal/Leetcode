class Solution:
    def rotate(self,nums:List[int],k:int)->List[int]:
        n = len(nums)
        k = k % n
        nums[:] = reversed(nums[:])
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return nums