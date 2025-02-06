from functools import lru_cache

def canConstruct(ransomNote, magazine):
    @lru_cache(None)  # Memoization to store results
    def helper(ransom, mag):
        if not ransom:  # If ransomNote is empty, return True
            return True
        if not mag:  # If magazine is empty, return False
            return False

        for i, char in enumerate(ransom):
            if char in mag:  
                # Remove the first occurrence of char from magazine
                new_mag = mag.replace(char, '', 1)
                # Recursively check with the updated ransomNote & magazine
                if helper(ransom[:i] + ransom[i+1:], new_mag):
                    return True

        return False  # If no valid way is found

    return helper(ransomNote, magazine)
