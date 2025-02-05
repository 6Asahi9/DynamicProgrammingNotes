def canSum(target, numbers, memo={}):
    if target in memo:
        return memo[target]  # Return cached result
    if target == 0:
        return True
    if target < 0:
        return False

    for num in numbers:
        remainder = target - num
        if canSum(remainder, numbers, memo):  # Recursive call with memo
            memo[target] = True  # Store result before returning
            return True

    memo[target] = False  # Store failure result
    return False

# Example usage
print(canSum(7, [2, 3]))  # True
print(canSum(7, [5, 3, 4, 7]))  # True
print(canSum(7, [2, 4]))  # False
print(canSum(8, [2, 3, 5]))  # True
print(canSum(300, [7, 14]))  # False (Runs much faster!)
