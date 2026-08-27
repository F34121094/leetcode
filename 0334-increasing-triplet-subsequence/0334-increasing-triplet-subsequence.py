class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        
        #紀錄目前最小的以及第二小的，由左到右
        for n in nums:
            if n <= first:  # 如果他比現在最小的小就交換
                first = n
            elif n <= second:    #如果他沒有比現在最小的小，但她比第二小的小也跟他交換
                second = n
            # 不用拿最原本最小的去看，因為後面的如果取代最小的，代表起點要重新計算
            else : return True
        
        return False
            