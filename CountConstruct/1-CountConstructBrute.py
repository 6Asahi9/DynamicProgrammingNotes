def countConstruct(target, wordBank):
    if target == "":
        return 1  # Found a valid way to construct the target
    
    totalWays = 0

    for word in wordBank:
        if target.startswith(word):  # Check if 'word' is a prefix
            suffix = target[len(word):]  # Remove the prefix
            numWaysForRest = countConstruct(suffix, wordBank)  # Recursive call
            totalWays += numWaysForRest  # Add up all valid ways

    return totalWays

# Test
print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))  # Output: 2
