class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        n_len = len(flowerbed)

        count = 0 
        for i in range(n_len):
            index_prev = i - 1
            index_next = i + 1

            prev = flowerbed[index_prev] if index_prev != -1 else 0
            next_ = flowerbed[index_next] if index_next != n_len else 0
            
            if not (flowerbed[i] + prev + next_):
                count += 1
                flowerbed[i] = 1
                if count >= n : break

        return count >= n
            
            