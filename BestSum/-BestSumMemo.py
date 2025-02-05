def bestSum(target, nums, memo={}):
    if target in memo:
        return memo[target]  # Return cached result
    if target == 0:
        return []  # Found a valid combination
    if target < 0:
        return None  # No valid combination

    shortest_combination = None  # Track the shortest valid combination

    for num in nums:
        remainder = target - num
        result = bestSum(remainder, nums, memo)  # Recursive call

        if result is not None:
            combination = result + [num]  # Create a new combination

            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination

    memo[target] = shortest_combination  # Store the result in memo
    return shortest_combination

# Test example
print(bestSum(7, [5, 3, 4, 7]))  # Output: [7]
print(bestSum(8, [2, 3, 5]))  # Output: [3, 5] (Shortest possible combination)
