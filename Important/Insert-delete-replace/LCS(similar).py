def longest_common_subsequence(text1: str, text2: str) -> int:
    """
    Finds the length of the longest common subsequence (LCS) between two strings.

    Args:
        text1: The first string.
        text2: The second string.

    Returns:
        The length of the LCS.
    """

    n = len(text1)
    m = len(text2)

    # Create a 2D array to store the lengths of LCSs for substrings
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # Iterate through the strings, comparing characters
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The bottom-right cell of the dp array holds the length of the LCS
    return dp[n][m]


# Example usage:
text1 = "abcde"
text2 = "ace"

lcs_length = longest_common_subsequence(text1, text2)
print(f"Length of the Longest Common Subsequence: {lcs_length}")  # Output: 3
