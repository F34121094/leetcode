class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        xa,ya,yb,xb = 0 , 0 , len(matrix) - 1 , len(matrix[0]) - 1 
        x_index , y_index = 0,0

        mode = 1

        result = [0] * (yb + 1) * (xb + 1)
        for i in range((yb + 1) * (xb + 1)):
            
            result[i] = matrix[y_index][x_index]

            if mode == 1:
                if x_index == xb:
                    mode = 2
                    ya += 1
                    y_index += 1
                else:
                    x_index += 1

            elif mode == 2:
                if y_index == yb:
                    mode = 3
                    xb -= 1
                    x_index -= 1
                else:
                    y_index += 1

            elif mode == 3:
                if x_index == xa:
                    mode = 4
                    yb -= 1
                    y_index -= 1
                else:
                    x_index -= 1

            else:
                if y_index == ya:
                    mode = 1
                    xa += 1
                    x_index += 1
                else:
                    y_index -= 1
        return result
