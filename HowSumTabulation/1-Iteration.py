Iteration Example (targetSum = 7, numbers = [2, 3])

Initial DP Table
[ [] , None, None, None, None, None, None, None]
  0     1     2     3     4     5     6     7  

-----------------------------------------------------------------------------
Step 1: Spread 2 and 3
[ [] , None, [2], [3], None, None, None, None]

-----------------------------------------------------------------------------
Step 2: Spread 2 and 3 again
[ [] , None, [2], [3], [2,2], [2,3], None, None]

-----------------------------------------------------------------------------
Step 3: Continue spreading
[ [] , None, [2], [3], [2,2], [2,3], [3,3], [3,2,2]]
Now, dp[7] contains [3,2,2], so 7 can be formed! 🎉
