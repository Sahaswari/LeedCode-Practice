class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum = nums[i]+nums[j]
                if sum == target:
                    print("[" +i +","+j+ "]")
                    break

            

            

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """