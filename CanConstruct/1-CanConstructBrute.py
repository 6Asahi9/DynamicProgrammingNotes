def canConstruct(ransomNote, magazine):
    # Base case: If ransom note is empty, return True
    if not ransomNote:
        return True
    
    # Iterate through the ransom note
    for i in range(len(ransomNote)):
        # Try to find each character in the magazine
        if ransomNote[i] in magazine:
            # Recur for the rest of the ransom note
            return canConstruct(ransomNote[:i] + ransomNote[i+1:], magazine.replace(ransomNote[i], '', 1))
    
    # If we couldn't find a letter in the magazine, return False
    return False

# Test Example
ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote, magazine))  # Output: True
