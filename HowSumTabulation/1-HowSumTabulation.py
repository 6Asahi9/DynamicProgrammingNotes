def howSum(targetSum, numbers):
    dp = [None] * (targetSum + 1)
    dp[0] = []  # Base case

    for i in range(targetSum + 1):
        if dp[i] is not None:
            for num in numbers:
                if i + num <= targetSum:
                    dp[i + num] = dp[i] + [num]  # Store combination

    return dp[targetSum]  # Returns a valid combination or None

# Example
print(howSum(7, [2, 3]))  # Output: [3, 2, 2] (or another valid combination)
