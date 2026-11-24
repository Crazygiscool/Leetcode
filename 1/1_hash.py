nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums, target):
        seen = {} # no need for typing for dict, just the {} works

        _seen = seen # definition so not looked up at diff mem loc. optimization
        for i,num in enumerate(nums):
            complement = target - num

            if complement in _seen:
                return[_seen[complement], i]

            _seen[num] = i
        return []

sol = Solution()

print(sol.twoSum(nums, target))
