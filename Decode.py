class Solution:
    def numDecodings(self, s):
        return self.helper(s, 0)

    def helper(self, s, i) :
        if i >= len(s):
            return 1
        if s[i] == '0':
            return 0
        ways = self.helper(s, i + 1)
        if i + 2 <= len(s) and int(s[i:i + 2]) <= 26:
            ways += self.helper(s, i + 2)
        return ways
s="226"
print(Solution().numDecodings(s))
