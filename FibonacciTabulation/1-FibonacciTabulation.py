def fib_propagation(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)  # Create an array of zeros
    dp[1] = 1  # Base case

    for i in range(n):  # Iterate over the array
        if i + 1 <= n:
            dp[i + 1] += dp[i]  # Add current to next position
        if i + 2 <= n:
            dp[i + 2] += dp[i]  # Add current to the one after next

    return dp[n]

# Example
n = 5
print(f"Fibonacci({n}) =", fib_propagation(n))
