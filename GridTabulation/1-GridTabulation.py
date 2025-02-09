def grid_traveler(m, n):
    dp = [[0] * (n+1) for _ in range(m+1)]
    dp[1][1] = 1
    
    for row in range(1, m+1):
        for col in range(1, n+1):
            if row == 1 and col == 1: continue
            dp[row][col] = (dp[row -1][col] if row > 1 else 0) + (dp[row][col - 1] if col > 1 else 0)
    return dp[row][col]
    
    
print(grid_traveler(3, 3))  # Output: 6
