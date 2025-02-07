def canConstruct(target, wordBank):
    dp = [False] * (len(target) + 1)
    dp[0] = True  # The empty string can always be constructed

    for i in range(len(target)):
        if dp[i]:  # If we can construct up to index i
            for word in wordBank:
                # Check if the substring starting at i matches the word
                if target[i:i + len(word)] == word:
                    dp[i + len(word)] = True

    return dp[len(target)]  # True if we can construct the whole target string

print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"] )) #output : False
