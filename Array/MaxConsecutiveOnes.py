#Given a binary array, find the maximum number of consecutive 1s in this array.
class Solution:
    def findMaxConsecutiveOnes(self,nums):
        max_sum=nums[0]
        counter=0
        for i in range(len(nums)):
            counter+=nums[i]
            if(counter>max_sum):
                max_sum=counter
            if(nums[i]==0):
                counter=0

        return max_sum
