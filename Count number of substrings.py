# User function Template for python3

class Solution:

    def substrCount(self, s, k):
        def atMostK(s, k):
            count = {}
            left = 0
            substr_count = 0
            for right in range(len(s)):
                count[s[right]] = count.get(s[right], 0) + 1
                while len(count) > k:
                    count[s[left]] -= 1
                    if count[s[left]] == 0:
                        del count[s[left]]
                    left += 1
                substr_count += right - left + 1
            return substr_count

        if k == 0:
            return 0

        return atMostK(s, k) - atMostK(s, k - 1)
S = "ecbaddce"
K = 3
print(Solution().substrCount(S,K))
