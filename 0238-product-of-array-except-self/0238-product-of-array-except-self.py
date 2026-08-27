class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = nums[:]
        suffix = nums[:]

        for i in range(n):
            prefix[i] *= prefix[i - 1] if i - 1 != -1 else 1
            suffix[n - i - 1] *= suffix[n - i] if n - i != n else 1
        
        ans = [0] * n
        
        for i in range(n):
            
            p = prefix[i - 1] if i - 1 != -1 else 1
            s = suffix[i + 1] if i + 1 != n else 1
            ans[i] = p * s
        
        return ans
        