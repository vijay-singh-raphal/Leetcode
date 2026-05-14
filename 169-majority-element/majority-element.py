class Solution:
    def majorityElement(self,nums:List[int])->int:
        moc = nums[0]
        co = 1
        for i in range(1,len(nums)):
            if nums[i] == moc:
                co = co + 1
            else:
                co = co - 1
                if co == 0:
                    moc = nums[i]
                    co = 1
        return moc