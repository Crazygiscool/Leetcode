nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}

        for i,num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return[seen[complement], i]

        seen[num] = i
        return []

sol = Solution()

print(sol.twoSum(nums, target))
