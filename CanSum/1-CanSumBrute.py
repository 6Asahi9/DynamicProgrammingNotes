def canSum(target, numbers):
    if target == 0:
        return True  # Base case: found a valid combination
    if target < 0:
        return False  # Base case: overshot the target

    for num in numbers:
        remainder = target - num
        if canSum(remainder, numbers):  # Recursively check
            return True  # Found a valid path

    return False  # No valid path found

# Example usage
print(canSum(7, [2, 3]))  # True (because 3+2+2 = 7)
print(canSum(7, [5, 3, 4, 7]))  # True (7 itself is in the array)
print(canSum(7, [2, 4]))  # False (can't make 7)
print(canSum(8, [2, 3, 5]))  # True (3+5 = 8)
print(canSum(300, [7, 14]))  # False (Takes a long time)
