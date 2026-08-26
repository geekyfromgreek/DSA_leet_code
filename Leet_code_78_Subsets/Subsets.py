class Solution:
    def subsets(self, nums):
        current = []
        result = []
        self.helper(nums, 0, current, result)
        return result

    def helper(self, nums, i, current, result):

        if i >= len(nums):
            result.append(current.copy())
            return

        current.append(nums[i])
        self.helper(nums, i + 1, current, result)


        current.pop()

        self.helper(nums, i + 1, current, result)