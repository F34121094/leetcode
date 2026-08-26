class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        left_index,right_index = 0,0
        last_right_one = 0
        count_1 = 0

        cur_len = float('inf')
        cur_string = ""

        while(1):
            if(count_1 < k and right_index != len(s)):
                if(s[right_index] == "1"):
                    count_1 += 1
                right_index += 1

            elif(count_1 == k):
                if(s[left_index] == "1"):
                    count_1 -= 1
                left_index += 1

            else: break
            
            if(count_1 == k):
                if(cur_len > right_index - left_index):
                    cur_len = right_index - left_index
                    cur_string = s[left_index : right_index : ]
                elif cur_len == right_index - left_index and cur_string > s[left_index : right_index : ]:
                    cur_string = s[left_index : right_index : ]


        return cur_string

        