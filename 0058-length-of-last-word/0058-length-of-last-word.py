class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """ 
        n = 0
        mode = 0 # 0代表現在遇到空格
        for char in s[::-1]:
            if char != ' ': #遇到字串
                if mode == 0:
                    mode = 1
                    n += 1
                else:
                    n += 1 
            else:           #遇到空格
                if mode == 0: continue
                else: break
        return n
              