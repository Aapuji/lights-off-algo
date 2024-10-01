import numpy as np

# Generate toggle matrix for given size n
def generate_toggle_matrix(n):
    size = n * n
    A = np.zeros((size, size), dtype=int)  # Pre-allocate matrix

    for i in range(n):
        for j in range(n):
            k = i * n + j
            A[k, k] = 1  # Toggle itself
            if i > 0:
                A[k, k - n] = 1  # Toggle the cell above
            if i < n - 1:
                A[k, k + n] = 1  # Toggle the cell below
            if j > 0:
                A[k, k - 1] = 1  # Toggle the cell to the left
            if j < n - 1:
                A[k, k + 1] = 1  # Toggle the cell to the right

    return A

# Efficient binary state generator
def generate_all_states(size):
    a = size * size
    return np.array(np.meshgrid(*[[0, 1]] * a)).T.reshape(-1, a)

# Size of grid
size = 3

# Toggle matrix T
T = np.array(generate_toggle_matrix(size), dtype=int)

# Identity matrix I
I = np.eye(size*size, dtype=int)

# Initialize matrix (I + T) mod 2
A = (I + T) % 2

# Print header
print(f'Grid size={size}x{size}, T size={size**2}x{size**2}')
print('Solution to (I + T)^n x = 0')
print('---------------------------')

# Generate all binary states for given size
all_states = generate_all_states(size)

# Precompute zero vector for comparison
zero_vector = np.zeros(size*size, dtype=int)

# Test all vectors for the given size
for arr in all_states:
    print(f'For x={arr}', end=': ')
    
    # Apply powers of A to x, and check when it results in zero vector
    n = 0
    current_x = arr
    M = 100  # max value to prevent infinite loop
    while not np.array_equal(current_x, zero_vector):
        current_x = np.dot(A, current_x) % 2
        n += 1
        if n > M:  # Avoid infinite loop
            break
    
    print(n)
