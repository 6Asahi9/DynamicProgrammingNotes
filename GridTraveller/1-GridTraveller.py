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

#----------------------------------------------------------------------------------------------------------------

#and dosen't matter if its a 3D grid either , just add a way to go forward 

def grid_traveler_3d(m, n, p, memo={}):
    # Base Case: If we reach a 1x1x1 grid, there's only 1 way
    if m == 1 and n == 1 and p == 1:
        return 1
    # If any dimension is 0, no possible way to travel
    if m == 0 or n == 0 or p == 0:
        return 0

    # Check if already computed
    if (m, n, p) in memo:
        return memo[(m, n, p)]
    
    # Recursive cases: Move in three directions (right, down, forward)
    memo[(m, n, p)] = (
        grid_traveler_3d(m - 1, n, p, memo) +  # Move down
        grid_traveler_3d(m, n - 1, p, memo) +  # Move right
        grid_traveler_3d(m, n, p - 1, memo)    # Move forward
    )
    
    return memo[(m, n, p)]

# Example Usage:
print(grid_traveler_3d(2, 2, 2))  # Output: 6
