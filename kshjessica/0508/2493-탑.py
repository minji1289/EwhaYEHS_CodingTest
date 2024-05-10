"""
[새로 배운 것]

The * operator in print(*answer) is known as the unpacking operator in Python. It is used to unpack the elements of the answer iterable (like a list or a tuple) into the print function.

This means that instead of printing the iterable as a single entity, it prints each element of the iterable separately. For example, if answer is a list of integers [1, 2, 3], print(*answer) will output 1 2 3 instead of [1, 2, 3].
"""

import sys

input = sys.stdin.readline

N = int(input())  # Number of towers
towers = list(map(int, input().split()))  # Heights of the towers

stack = []  # Stack to store tower indices and heights
answer = [0] * N  # List to store the answer

for i in range(N):
    while stack:
        if stack[-1][1] > towers[i]:  # If the height of the tower in the stack is greater than the current tower
            answer[i] = stack[-1][0] + 1  # Set the answer for the current tower as the index of the tower in the stack + 1
            break
        else:
            stack.pop()  # Remove towers from the stack until a tower with greater height is found

    stack.append((i, towers[i]))  # Add the current tower to the stack

print(*answer)  # Print the answer
