def canConstruct(ransomNote, magazine):
    memo = {}

    def helper(ransomNote, magazine):
        # If ransomNote is empty, we can construct it (base case)
        if not ransomNote:
            return True
        
        # If this subproblem has already been computed, return its result
        if (ransomNote, magazine) in memo:
            return memo[(ransomNote, magazine)]
        
        # Try to find each character of ransomNote in magazine
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine:
                # Recurse for the rest of the ransom note with the character removed from magazine
                result = helper(ransomNote[:i] + ransomNote[i+1:], magazine.replace(ransomNote[i], '', 1))
                if result:
                    # Store the result in the memo dictionary before returning it
                    memo[(ransomNote, magazine)] = True
                    return True
        
        # If we couldn't find a match for any character, store the result as False
        memo[(ransomNote, magazine)] = False
        return False
    
    return helper(ransomNote, magazine)

# Test Example
ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))  # Output: True
