def countConstructDP(target, wordBank, memo={}):
    if target in memo:
        return memo[target]  # Return memoized result
    
    if target == "":
        return 1  # Found a valid way

    totalWays = 0

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]  
            numWaysForRest = countConstructDP(suffix, wordBank, memo)  
            totalWays += numWaysForRest  

    memo[target] = totalWays  # Store in memo
    return totalWays

# Test
print(countConstructDP("purple", ["purp", "p", "ur", "le", "purpl"]))  # Output: 2
