class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        l,r = 0 , len(s)-1
        s_list = list(s)

        while(l < r):
            while s_list[l] not in vowels and l < r: l += 1
            while s_list[r] not in vowels and l < r: r -= 1

            s_list[l],s_list[r] = s_list[r],s_list[l]
            l += 1
            r -= 1
        return "".join(s_list)
                
            
        