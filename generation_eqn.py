import numpy as np
import itertools as it

# Generate toggle matrix for given size n
def generate_toggle_matrix(n):
    size = n * n
    A = [[0] * size for _ in range(size)]

    for i in range(n):
        for j in range(n):
            k = i * n + j
            A[k][k] = 1  # Toggle itself
            if i > 0:
                A[k][k - n] = 1  # Toggle the cell above
            if i < n - 1:
                A[k][k + n] = 1  # Toggle the cell below
            if j > 0:
                A[k][k - 1] = 1  # Toggle the cell to the left
            if j < n - 1:
                A[k][k + 1] = 1  # Toggle the cell to the right

    return A

# Find n in (I + T)^n x = 0
# Returns n and current_x to check it
def find_n(x):
    global size, A
    n = 0
    current_x = x
    M = 100 # max value to not have infinite loop
    while not np.array_equal(current_x, np.zeros(size, dtype=int)):
        current_x = np.dot(A, current_x) % 2
        n += 1
        if n > M:  # Avoid infinite loop
            break
    
    return (n, current_x)

def test_all_states():
    global size
    
    a = size*size
    
    return [
        np.array([int(i) for i in bin(x)[2:].zfill(a)])
        for x in range(0, 2**a)
    ]
    
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

# Test all vectors for the given size
for arr in test_all_states():
    print(f'For x={arr}', end=': ')
    
    n = 0
    current_x = arr
    M = 100 # max value to not have infinite loop
    while not np.array_equal(current_x, np.zeros(size*size, dtype=int)):
        current_x = np.dot(A, current_x) % 2
        n += 1
        if n > M:  # Avoid infinite loop
            break
    
    print(n)
    
    # print (n, current_x)
