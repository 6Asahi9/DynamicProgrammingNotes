def bestSum(targetSum, numbers):
    dp = [None] * (targetSum + 1)
    dp[0] = []  # Base case

    for i in range(targetSum + 1):
        if dp[i] is not None:
            for num in numbers:
                if i + num <= targetSum:
                    new_combination = dp[i] + [num]  # Extend the current combination
                    # Update only if it's shorter than the existing one
                    if dp[i + num] is None or len(new_combination) < len(dp[i + num]):
                        dp[i + num] = new_combination

    return dp[targetSum]  # Returns shortest combination or None

# Example
print(bestSum(7, [5, 3, 4, 7]))  # Output: [7] (since it's the shortest)
print(bestSum(8, [2, 3, 5]))     # Output: [3, 5] (shortest way to make 8)
