#now we need Dp cos basic Fibonacci can do simple numbers but it will get stuck on bigger numbers like 50
#thats why we use memo or a place to store the numbers we have already seen 

def fib(n, memo={}):
    # Base case
    if n <= 1:
        return n
    
    # Check if the value is already in the memo dictionary
    if n in memo:
        return memo[n]
    
    # If not in memo, calculate it and store the result in memo
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    
    return memo[n]

# Test the function
print(fib(50))  # Output will be the 12586269025
