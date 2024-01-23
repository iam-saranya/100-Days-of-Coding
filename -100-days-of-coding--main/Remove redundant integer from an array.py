class Solution:
    def removeDuplicates(self, nums):
        nums[:] = sorted(set(nums))
        return len(nums)

nums = [1, 1, 2]
solution = Solution()
k = solution.removeDuplicates(nums)
print("Output k:", k)
print("Modified nums:", nums[:k])
