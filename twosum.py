class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} 

        for i in range(len(nums)):

            diff = target - nums[i]

            if diff in seen:
                y = [seen[diff], i]
                return y

            else:
                seen[nums[i]] = i