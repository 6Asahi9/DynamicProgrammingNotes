def canSum(target, numbers):
    dp = [False] * (target + 1)
    dp[0] = True  # Base case: sum of 0 is always possible

    for i in range(target + 1):
        if dp[i]:  # If the current sum is possible
            for num in numbers:
                if i + num <= target:  # Don't go out of bounds
                    dp[i + num] = True  # Mark this sum as possible

    return dp[target]  # Final answer: Can we reach 'target'?
