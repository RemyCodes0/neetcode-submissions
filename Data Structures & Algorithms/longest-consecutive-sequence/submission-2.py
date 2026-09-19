class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 0:
            return 0
        count = 1
        longest = 1
        for i in range(len(nums)):

            if i+1 < len(nums) and nums[i] == nums[i+1]:
                continue
            if i+1 < len(nums) and nums[i] + 1 == nums[i+ 1]:
                count+=1
            else:
                count=1
            longest = max(longest, count)
            
        return longest