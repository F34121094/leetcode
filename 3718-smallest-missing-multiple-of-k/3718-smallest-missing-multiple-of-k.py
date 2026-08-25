class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        time = 1
        num_set = set(nums)
        while True:
            if k * time not in num_set: return k * time
            else: time += 1