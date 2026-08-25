class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        sum_list = [0] * len(nums)
        sum_list[0] = nums[0]
        print(sum_list[0])
        for index in range(1,len(nums)):
            sum_list[index] += sum_list[index - 1] + nums[index]
            print(sum_list[index])

        count = 0
        for i in range(len(sum_list)-1):            
            if sum_list[i] >= (sum_list[-1] - sum_list[i]) : count += 1

        return count