canSum(7, [2, 3])
1️⃣
We create a boolean list dp of size target + 1 (8 in this case)
Index (Sum)  0   1   2   3   4   5   6   7  
dp          [T,  F,  F,  F,  F,  F,  F,  F]  

-----------------------------------------------------------------------------------------------------------
2️⃣ Start Iterating
We go through the list and update possible sums.

    Iteration: i = 0 (Base Case)
    dp[0] = True, so we process it.
    We try adding 2 and 3:
        dp[0 + 2] = dp[2] = True
        dp[0 + 3] = dp[3] = True
dp          [T,  F,  T,  T,  F,  F,  F,  F]  

-----------------------------------------------------------------------------------------------------------
    Iteration: i = 1
dp[1] = False, so skip this index
    Iteration: i = 2
    dp[2] = True, so process it.
    We try adding 2 and 3:
      dp[2 + 2] = dp[4] = True
      dp[2 + 3] = dp[5] = True
dp          [T,  F,  T,  T,  T,  T,  F,  F]  

-----------------------------------------------------------------------------------------------------------
      Iteration: i = 3
    dp[3] = True, so process it.
    We try adding 2 and 3:
      dp[3 + 2] = dp[5] = True (already True)
      dp[3 + 3] = dp[6] = True
dp          [T,  F,  T,  T,  T,  T,  T,  F]  

-----------------------------------------------------------------------------------------------------------
      Iteration: i = 4
    dp[4] = True, so process it.
    We try adding 2 and 3:
      dp[4 + 2] = dp[6] = True (already True)
      dp[4 + 3] = dp[7] = True 🎯 (Target reached!)
dp          [T,  F,  T,  T,  T,  T,  T,  T]  
Since dp[7] = True, we return True! ✅

