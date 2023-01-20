class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        l1=[]
        for i in range(len(nums)):
            if len(nums)==0:
                return 0
            elif nums[i]==1:
                count+=1
                l1.append(count)
            elif nums[i]==0:
                count=0
                l1.append(count)
        return max(l1)
