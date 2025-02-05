def howSum(target, nums):
    if target == 0:  # If we reached target 0, we found a solution
        return []
    if target < 0:  # If the target goes negative, no solution exists
        return None

    for num in nums:
        remainder = target - num  # Subtract the current number from the target
        result = howSum(remainder, nums)  # Recursively check the remainder

        if result is not None:  # If we found a solution
            return [num] + result  # Return the number combined with the result

    return None  # If no solution is found

# Test example
print(howSum(7, [2, 3]))  # Output: [3, 2] or [2, 3]
