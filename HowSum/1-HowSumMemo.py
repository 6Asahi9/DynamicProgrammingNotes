def howSum(target, nums, memo = {}):
    if target in memo: return memo[target]
    if target == 0:  # If we reached target 0, we found a solution
        return []
    if target < 0:  # If the target goes negative, no solution exists
        return None

    for num in nums:
        remainder = target - num  # Subtract the current number from the target
        result = howSum(remainder, nums, memo)  # Recursively check the remainder

        if result is not None:  # If we found a solution
            memo[target] = [num] + result  # Return the number combined with the result
            return memo[target]
    memo[target] = None
    return None  # If no solution is found

# Test example
print(howSum(7, [2, 3]))  # Output: [2,2,3]
