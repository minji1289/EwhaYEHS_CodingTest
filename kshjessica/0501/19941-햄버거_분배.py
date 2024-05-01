n, k = map(int, input().split())  # Read integers n and k from input
table = list(input())  # Read a string and convert it to a list of characters
answer = 0  # Initialize the answer variable to 0

for i in range(n):  # Iterate over the indices from 0 to n-1
    if table[i] == 'P':  # If the current character is 'P'
        for j in range(max(0, i-k), min(n, i+k+1)):  # Iterate over the indices within the range [max(0, i-k), min(n, i+k+1))
            if table[j] == 'H':  # If the character at index j is 'H'
                table[j] = 'X'  # Replace the character at index j with 'X'
                answer += 1  # Increment the answer variable by 1
                break  # Exit the inner loop

print(answer)  # Print the value of the answer variable