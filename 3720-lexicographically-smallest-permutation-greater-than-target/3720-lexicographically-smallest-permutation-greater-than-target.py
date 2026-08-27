class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s_count = Counter(s)
        for i in range(n-1 , -1 , -1):

            prefix = target[:i]
            prefix_count = Counter(prefix)

            possible = True
            for char, count in prefix_count.items():
                if s_count[char] < count:
                    possible = False
                    break

            if possible == False: continue

            avalible = []

            for char in s_count:
                rem = s_count[char] - prefix_count.get(char,0)
                if rem > 0:
                    avalible.extend([char] * rem)

            target_c = target[i]
            valid_char = [c for c in avalible if c > target_c]

            if valid_char:
                best_char = min(valid_char)

                avalible.remove(best_char)
                avalible.sort()

                return prefix + best_char + "".join(avalible)
        return ""

            