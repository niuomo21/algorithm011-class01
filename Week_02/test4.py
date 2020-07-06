class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            res = target - nums[i]
            #做差 结果在数组中
            if res in nums:
                j = nums.index(res)
                #一个数只能用一次
                if i == j:
                    continue
                else:
                    return i,j
            else:
                continue
