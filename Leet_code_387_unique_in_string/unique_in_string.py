class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for i in range(len(s)):
            if s[i] in count:
                count[s[i]] = count[s[i]] + 1
            else:
                count[s[i]] = 1

        for i in range(len(s)):
            if count[s[i]] == 1:
                return i

        return -1