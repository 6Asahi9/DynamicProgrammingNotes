def fib_three_pointers(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)  # Create an array filled with zeros
    dp[1] = 1  # Base case

    for curr in range(n - 1):  # Go up to n-1 to avoid index errors
        next1 = curr + 1
        next2 = curr + 2

        dp[next1] += dp[curr]  # Add current value to next1
        if next2 <= n:
            dp[next2] += dp[curr]  # Add current value to next2

    return dp[n]

# Example
n = 10
print(f"Fibonacci({n}) =", fib_three_pointers(n))
