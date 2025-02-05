def bestSum(target, nums):
    if target == 0:
        return []  # Found a valid combination
    if target < 0:
        return None  # No valid combination

    shortest_combination = None  # Track the shortest valid combination

    for num in nums:
        remainder = target - num
        result = bestSum(remainder, nums)  # Recursive call

        if result is not None:  # If we found a valid combination
            combination = result + [num]  # Create a new combination

            # If it's the shortest so far, update it
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination

    return shortest_combination  # Return the shortest valid combination

# Test example
print(bestSum(7, [5, 3, 4, 7]))  # Output: [7] (Shortest possible combination)
