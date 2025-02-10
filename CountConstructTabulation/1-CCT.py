def count_construct(target, wordBank):
    dp = [0] * (len(target) + 1)
    dp[0] = 1  # Base case: There's 1 way to construct an empty string

    for i in range(len(target) + 1):
        if dp[i] > 0:  # Only process if this prefix is constructible
            for word in wordBank:
                if target[i:].startswith(word):  # If word fits at position i
                    dp[i + len(word)] += dp[i]  # Add ways from dp[i]

    return dp[len(target)]  # Final answer: How many ways to construct full string?
--------------------------------------------------------------------------------------------------------
Walkthrough with count_construct("purple", ["purp", "p", "ur", "le", "purpl"])

dp = [1, 0, 0, 0, 0, 0, 0]
#      0   1   2   3   4   5   6
#      ""  "p" "pu" "pur" "purp" "purpl" "purple"

--------------------------------------------------------------------------------------------------------
Processing Words:

"p" fits at dp[0], so dp[1] += 1
"purp" fits at dp[0], so dp[4] += 1
"ur" fits at dp[1], so dp[3] += 1
"p" fits at dp[2], so dp[3] += 1
"le" fits at dp[4], so dp[6] += dp[4]
"le" fits at dp[5], so dp[6] += dp[5]

--------------------------------------------------------------------------------------------------------
dp = [1, 1, 0, 2, 1, 0, 2]
Since dp[6] = 2, we return 2.
