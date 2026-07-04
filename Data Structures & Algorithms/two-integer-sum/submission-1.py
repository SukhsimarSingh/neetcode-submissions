class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        # 2, 7, 11, 15
        # target = 9
        # 9-2 = 7, 9-7 = 2, 9-11 = -2, 9-15 = -6
        # diff = {7:0, 2:1, -2:2, -6:3}
        # Save the differences, not check if difference is in remaining list
        # The problem, we need to know the index

        for i in range(len(nums)):
            if nums[i] in diff:
                return sorted([i, diff[nums[i]]])

            d = target - nums[i]
            diff[d] = i
        