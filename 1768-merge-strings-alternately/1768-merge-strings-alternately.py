class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index_1 , index_2 = 0,0
        result = ""
        for i in range(max(len(word1),len(word2))):
            c1 = word1[index_1] if index_1 < len(word1) else ""
            c2 = word2[index_2] if index_2 < len(word2) else ""
            index_1 += 1
            index_2 += 1
            result += c1 + c2
        return result
            