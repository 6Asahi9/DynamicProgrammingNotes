# 5. Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0: 
            return ""  # Edge case: if the string is empty, return an empty string

        # Create a DP table where dp[i][j] will be True if substring s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]
        start = 0  # Stores the starting index of the longest palindrome found
        max_length = 1  # Stores the length of the longest palindrome found

        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True

        # Check for substrings of length 2 (two consecutive characters)
        for i in range(n - 1):
            if s[i] == s[i + 1]:  # If two adjacent characters are the same, it's a palindrome
                dp[i][i + 1] = True
                start = i  # Update starting index
                max_length = 2  # Update max palindrome length
        
        # Check for substrings of length 3 or more
        for length in range(3, n + 1):  # Start from length 3 up to full string length
            for i in range(n - length + 1):  # i is the starting index of the substring
                j = i + length - 1  # j is the ending index of the substring

                # A substring s[i:j] is a palindrome if:
                # 1. The first and last characters match (s[i] == s[j])
                # 2. The inner substring s[i+1:j-1] is also a palindrome (dp[i+1][j-1] is True)
                if s[i] == s[j] and dp[i + 1][j - 1]:  
                    dp[i][j] = True
                    start = i  # Update the starting index of the longest palindrome found
                    max_length = length  # Update the max palindrome length

        # Return the longest palindromic substring
        return s[start:start + max_length]
