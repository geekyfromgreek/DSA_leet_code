class Solution:
    def runningSum(self, nums):
        running_Sum=0
        result=[]  
        for i in range (len(nums)):   
            running_Sum = running_Sum + nums[i]
            result.append(running_Sum)      
        return result