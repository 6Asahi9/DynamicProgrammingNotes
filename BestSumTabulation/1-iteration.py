Initial Setup
  We create an array dp of size targetSum + 1 (8 in this case).
  dp[0] = [] because sum 0 is possible with an empty list.
  The rest of the values start as None (meaning, we haven't found a way to reach them yet)

Index:  0     1     2     3     4     5     6     7
----------------------------------------------------
dp:   [ [] , None, None, None, None, None, None, None]

---------------------------------------------------------------------------------------------------
Step 1: Processing dp[0] (Current sum = 0)
We spread all numbers from 0:
0 + 5 = 5 → dp[5] = [5]
0 + 3 = 3 → dp[3] = [3]
0 + 4 = 4 → dp[4] = [4]
0 + 7 = 7 → dp[7] = [7]

Index:  0     1     2     3     4     5     6     7
----------------------------------------------------
dp:   [ [] , None, None, [3] , [4] , [5] , None, [7] ]

---------------------------------------------------------------------------------------------------
Step 2: Processing dp[3] (Current sum = 3)
We spread from 3:
3 + 5 = 8 (out of bounds, ignored)
3 + 3 = 6 → dp[6] = [3, 3]
3 + 4 = 7 → dp[7] = [3, 4] (But [7] is shorter, so we keep [7])

Index:  0     1     2     3     4     5     6     7
----------------------------------------------------
dp:   [ [] , None, None, [3] , [4] , [5] , [3,3] , [7] ]

---------------------------------------------------------------------------------------------------
Step 3: Processing dp[4] (Current sum = 4)
We spread from 4:
4 + 5 = 9 (out of bounds, ignored)
4 + 3 = 7 → dp[7] = [4, 3] (Again, [7] is shorter, so we keep [7])
4 + 4 = 8 (out of bounds, ignored)

No changes to dp table.

---------------------------------------------------------------------------------------------------
Step 4: Processing dp[5] (Current sum = 5)
We spread from 5:
5 + 5 = 10 (out of bounds, ignored)
5 + 3 = 8 (out of bounds, ignored)
5 + 4 = 9 (out of bounds, ignored)

No changes to dp table.
---------------------------------------------------------------------------------------------------
Step 5: Processing dp[6] (Current sum = 6)
We spread from 6:
6 + 5 = 11 (out of bounds, ignored)
6 + 3 = 9 (out of bounds, ignored)
6 + 4 = 10 (out of bounds, ignored)

No changes to dp table.

---------------------------------------------------------------------------------------------------
Final DP Table
Index:  0     1     2     3     4     5     6     7
----------------------------------------------------
dp:   [ [] , None, None, [3] , [4] , [5] , [3,3] , [7] ]

dp[7] = [7], so the shortest way to get 7 is [7]!
