from collections import deque
from sys import stdin


def solution(N, K, A):
    answer = 0
    belt = deque([False] * N)  # Create a deque representing the conveyor belt with N slots, initially empty

    while True:
        answer += 1  # Increment the answer counter by 1

        A.rotate(1)  # Rotate the durability list A by 1 to simulate the movement of the conveyor belt
        belt.rotate(1)  # Rotate the belt deque by 1 to simulate the movement of the conveyor belt

        belt[N-1] = False  # Set the last slot of the belt to False, indicating that it is empty

        for i in range(N-2, -1, -1):
            # Check if there is a robot on the current slot and the next slot is empty and the durability of the next slot is greater than 0
            if belt[i] and not belt[i+1] and A[i+1] > 0:
                belt[i], belt[i+1] = False, True  # Move the robot from the current slot to the next slot
                A[i+1] -= 1  # Decrease the durability of the next slot by 1

        belt[N-1] = False  # Set the last slot of the belt to False, indicating that it is empty

        if A[0] > 0:
            belt[0] = True  # Place a robot on the first slot of the belt
            A[0] -= 1  # Decrease the durability of the first slot by 1

        if A.count(0) >= K:  # Check if the number of slots with durability 0 is greater than or equal to K
            break  # If so, break out of the loop

    return answer

N, K = map(int, stdin.readline().split())  # Read the values of N and K from input
A = deque(list(map(int, stdin.readline().split())))  # Read the durability values of the slots from input and create a deque

response = solution(N, K, A)  # Call the solution function with the provided inputs
print(response)  # Print the result
