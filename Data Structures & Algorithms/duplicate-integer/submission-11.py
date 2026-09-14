class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            number = nums.count(i)
            if number >=2:
                return True
        return False