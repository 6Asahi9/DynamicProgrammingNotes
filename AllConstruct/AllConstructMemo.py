def allConstructDP(target, wordBank, memo={}):
    if target in memo:
        return memo[target]  # Return memoized result
    
    if target == "":
        return [[]]  # Base case: One valid way (empty list)

    result = []

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word):]  
            suffixWays = allConstructDP(suffix, wordBank, memo)  
            for way in suffixWays:
                result.append([word] + way)  

    memo[target] = result  # Store result in memo
    return result

# Test
print(allConstructDP("purple", ["purp", "p", "ur", "le", "purpl"], {}))
#output
#[['purp', 'le'], ['p', 'ur', 'p', 'le']]
