def all_construct(target, wordBank):
    dp = [[] for _ in range(len(target) + 1)]
    dp[0] = [[]]  # Base case: One way to construct an empty string (do nothing)

    for i in range(len(target) + 1):
        if dp[i]:  # If this prefix can be constructed
            for word in wordBank:
                if target[i:].startswith(word):  # If word fits at position i
                    new_combinations = [sublist + [word] for sublist in dp[i]]
                    dp[i + len(word)].extend(new_combinations)

    return dp[len(target)]  # Final answer: List of all ways to construct full target
-----------------------------------------------------------------------------------------------------------
 Walkthrough with all_construct("purple", ["purp", "p", "ur", "le", "purpl"])
dp = [ [[]], [], [], [], [], [], [] ]
#        0      1    2    3    4    5    6
#       ""     "p"  "pu" "pur" "purp" "purpl" "purple"

-----------------------------------------------------------------------------------------------------------
Processing Words:

"p" fits at dp[0], so dp[1] = [["p"]]
"purp" fits at dp[0], so dp[4] = [["purp"]]
"ur" fits at dp[1], so dp[3] = [["p", "ur"]]
"le" fits at dp[4], so dp[6] = [["purp", "le"]]
"p" fits at dp[2], so dp[3] = [["p", "ur"]]
"le" fits at dp[5], so dp[6] = [["purp", "le"], ["p", "ur", "p", "le"]]
-----------------------------------------------------------------------------------------------------------
dp = [
    [[]],  # dp[0]  → [""]
    [["p"]],  # dp[1]  → ["p"]
    [],  # dp[2]  → (empty)
    [["p", "ur"]],  # dp[3]  → ["p", "ur"]
    [["purp"]],  # dp[4]  → ["purp"]
    [],  # dp[5]  → (empty)
    [["purp", "le"], ["p", "ur", "p", "le"]]  # dp[6]  → [["purp", "le"], ["p", "ur", "p", "le"]]
]
-----------------------------------------------------------------------------------------------------------
Since dp[6] = [["purp", "le"], ["p", "ur", "p", "le"]], we return:
[
    ["purp", "le"],
    ["p", "ur", "p", "le"]
]
