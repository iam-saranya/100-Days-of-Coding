class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
       
        return []
if __name__ == "__main":
    solution = Solution()
    param1 = [2, 7, 11, 15]
    param2 = 9
    ret = solution.twoSum(param1, param2)
    print(ret)
