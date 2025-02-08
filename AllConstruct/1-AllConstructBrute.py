def allConstruct(target, wordBank):
    if target == "":
        return [[]]  # Base case: One valid way (empty list)

    result = []

    for word in wordBank:
        if target.startswith(word):  # If word is a prefix
            suffix = target[len(word):]  # Remove the prefix
            suffixWays = allConstruct(suffix, wordBank)  # Get ways to construct the suffix
            for way in suffixWays:
                result.append([word] + way)  # Append word to each way

    return result

# Test
print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
#output
#[['purp', 'le'], ['p', 'ur', 'p', 'le']]
