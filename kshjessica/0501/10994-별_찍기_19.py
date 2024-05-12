N = int(input())

# Calculate the size of the pattern
size = 4 * N - 3

# Create the pattern(original version)
'''
pattern = []
for _ in range(size):
    pattern.append([' '] * size)
'''
# Create the pattern(compact version)
pattern = [[' '] * size for _ in range(size)]

# Recursive function to fill the pattern
def fill_pattern(x, y, n):
    if n == 1:
        pattern[x][y] = '*'
        return

    # Fill the outer square
    for i in range(x, x + 4 * n - 3):
        pattern[x][i] = '*'
        pattern[x + 4 * n - 4][i] = '*'
        pattern[i][y] = '*'
        pattern[i][y + 4 * n - 4] = '*'

    # Fill the inner square
    fill_pattern(x + 2, y + 2, n - 1)

# Fill the pattern recursively
fill_pattern(0, 0, N)

# Print the pattern
for row in pattern:
    print(''.join(row))