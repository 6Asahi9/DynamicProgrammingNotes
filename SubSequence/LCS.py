def longest_common_subsequence(s1, s2):
    row, col = len(s1), len(s2)

    # Step 1: Create DP Table (row+1 x col+1)
    dp = [[0] * (col + 1) for _ in range(row + 1)]

    # Step 2: Fill DP Table
    for i in range(1, row + 1):
        for j in range(1, col + 1):
            if s1[i - 1] == s2[j - 1]:  # Match → add diagonal +1
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:  # Mismatch → take max from top or left
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Step 3: Backtracking to find the LCS
    i, j = row, col
    lcs = []

    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:  # Match → move diagonally ↖️
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:  # Move Up ⬆️
            i -= 1
        else:  # Move Left ⬅️
            j -= 1

    lcs.reverse()  # Since we collected it backwards
    return "".join(lcs)

# Example Run
s1 = "cab"
s2 = "abac"
print(longest_common_subsequence(s1, s2))  # Output: "ab"
