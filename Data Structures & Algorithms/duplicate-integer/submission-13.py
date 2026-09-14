class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        seen = set()
        i = 0
        while  i<=len(nums)-1 and nums[i] not in seen :
            seen.add(nums[i])
            i+=1
        if len(seen) == len(nums):
            return False
        return True