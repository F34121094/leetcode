class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if s.count("1") < k: return ""
        left = 0
        count_1 = 0
        ans = s
        

        for right, x in enumerate(s):
            if x == "1":
                count_1 += 1
            while(count_1 > k or s[left] == "0"):
                count_1 -= int(s[left])
                left += 1
            
            if count_1 == k:
                t = s[left : right+1]
                if len(ans) > len(t) or (len(ans) == len(t) and t < ans):
                    ans = t
        return ans

        