nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums, target):
        seen: dict[int, int] = {}

        _nums = nums # definition so not looked up at diff mem loc. optimization
        _seen = seen # definition so not looked up at diff mem loc. optimization
        for i,num in enumerate(_nums):
            complement = target - num

            if complement in seen:
                return[seen[complement], i]

            seen[num] = i
        return []

sol = Solution()

print(sol.twoSum(nums, target))
