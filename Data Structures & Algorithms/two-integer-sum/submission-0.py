class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        n = len(nums)
        for i in range(0,n):
            comp = target - nums[i]

            if comp in hash_map:
                return [hash_map[comp],i]
            hash_map[nums[i]] = i