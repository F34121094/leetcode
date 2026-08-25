class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s == p: return True

        p_index = 0
        s_index = 0

        star_index = -1
        s_match = -1

        while s_index < len(s):
            
            if p_index < len(p) and (p[p_index] == "?" or s[s_index] == p[p_index]):
                print(f"s[{s_index}] = {s[s_index]} , p[{p_index}] = {p[p_index]}")
                s_index += 1
                p_index += 1
            
            elif p_index < len(p) and p[p_index] == "*":
                print(f"s[{s_index}] = {s[s_index]} , p[{p_index}] = {p[p_index]}")
                star_index = p_index
                s_match = s_index
                p_index += 1    # 第一次遇到的時候先看完全不配對的

            elif star_index != -1:  #代表有存檔
                s_match += 1    # * 多跟 s 配對一個
                s_index = s_match
                p_index = star_index

            else: return False  #代表沒有存檔

        while p_index < len(p) and p[p_index] == "*": p_index += 1

        return p_index == len(p)


                  

                
            
            
            
            



            
        
            

        
        