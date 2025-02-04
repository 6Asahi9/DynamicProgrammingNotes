def grid_traveler(m, n, memo={}):
    # Base cases
    if m == 1 and n == 1:
        return 1  # Only one way to be in a 1x1 grid (stay there)
    if m == 0 or n == 0:
        return 0  # No way to travel if any dimension is 0
    
    # Check if the result is already in memo
    if (m, n) in memo:
        return memo[(m, n)]
    
    # Calculate by moving right and down, and store the result in memo
    memo[(m, n)] = grid_traveler(m - 1, n, memo) + grid_traveler(m, n - 1, memo)
    
    return memo[(m, n)]

# Example Usage
print(grid_traveler(2, 3))  # Output: 3
