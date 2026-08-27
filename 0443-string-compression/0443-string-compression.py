class Solution:
    def compress(self, chars: List[str]) -> int:
        
        read,write = 0,0
        
        chars_len = len(chars)
        
        while read < chars_len:
            char = chars[read]
            count = 0

            while read < chars_len and char == chars[read]:
                read += 1
                count += 1
            
            chars[write] = char
            write += 1
            if count != 1:
                for val in list(str(count)):
                    chars[write] = val
                    write += 1
        
        return write
    