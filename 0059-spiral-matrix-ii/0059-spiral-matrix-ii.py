class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        x = 0
        y = 0
        mode = 1
        iterate = 0
        # 用mode紀錄上下左右
        result = [[0]*n for _ in range(n)]

        for i in range(n*n):   #1 , 3為可能結束的時候
            val = i+1
            result[y][x] = val
            
            if mode == 1:
                if x + 1 == n - iterate:
                    y += 1
                    mode = 2
                else: x += 1
                continue             

            elif mode == 2:
                if y + 1 == n - iterate:
                    x -= 1
                    mode = 3
                else: y += 1
            elif mode == 3:
                if x - 1 == -1 + iterate:
                    y -= 1
                    mode = 4
                    iterate += 1
                else: x -= 1
                continue   

            else:
                if y - 1 == -1 + iterate:
                    x += 1
                    mode = 1
                else: y -= 1

        return result