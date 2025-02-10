def can_construct(target, wordBank):
    dp = [False] * (len(target) + 1)
    dp[0] = True  # Base case: Empty string can always be constructed

    for i in range(len(target) + 1):
        if dp[i]:  # Only process if this prefix is constructible
            for word in wordBank:
                if target[i:].startswith(word):  # If word fits at position i
                    dp[i + len(word)] = True

    return dp[len(target)]  # Final answer: Can we construct the full string?

----------------------------------------------------------------------------------
Step Walkthrough with can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])
dp = [True, False, False, False, False, False, False]
#      0     1      2      3      4      5      6
#      ""   "a"    "ab"   "abc"  "abcd" "abcde" "abcdef"
----------------------------------------------------------------------------------

Processing Words:

"ab" fits at dp[0], so dp[2] = True
"abc" fits at dp[0], so dp[3] = True
"abcd" fits at dp[0], so dp[4] = True
"cd" fits at dp[2], so dp[4] = True (already True)
"def" fits at dp[3], so dp[6] = True 
----------------------------------------------------------------------------------

dp = [True, False, True, True, True, False, True]
Since dp[6] = True, we return True.
