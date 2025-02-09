def fib_tabulation(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)  # Create an array to store Fibonacci values
    dp[0], dp[1] = 0, 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Example
n = 10
print(f"Fibonacci({n}) =", fib_tabulation(n))
