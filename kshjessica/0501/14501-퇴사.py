N = int(input())  # Read the value of N from input and convert it to an integer

schedule = []  # Create an empty list to store the schedule

for _ in range(N):  # Iterate N times
    T, P = map(int, input().split())  # Read the values of T and P from input and convert them to integers
    
    schedule.append((T, P))  # Append a tuple of (T, P) to the schedule list

dp = [0] * (N + 1)  # Create a list of zeros with length N+1 to store the maximum profit

for i in range(N - 1, -1, -1):  # Iterate from N-1 to 0 in reverse order
    if i + schedule[i][0] <= N:  # Check if the current day + the duration of the current schedule is less than or equal to N
        dp[i] = max(schedule[i][1] + dp[i + schedule[i][0]], dp[i + 1])  # Calculate the maximum profit by either taking the current schedule or skipping it
    else:
        dp[i] = dp[i + 1]  # If the current schedule cannot be completed before the last day, skip it and take the profit from the next day

print(dp[0])  # Print the maximum profit