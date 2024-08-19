


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        dp = [[False] * n for _ in range(n)]
        start = 0
        maxLength = 1

        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = True

        # Check for a palindrome of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                maxLength = 2

        # Check for lengths greater than 2
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start = i
                    maxLength = length

        return s[start:start + maxLength]


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    input_string = input("Enter a string: ")  # Accept input from the user
    result = sol.longestPalindrome(input_string)
    print("Longest Palindromic Substring:", result)
