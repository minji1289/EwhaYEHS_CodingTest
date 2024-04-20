# Number of regions
n = int(input())
# Budget requests for each region
budget = list(map(int, input().split()))
# Total budget
m = int(input())

start, end = 0, max(budget)  # Initialize start and end points for binary search
total_budget = 0  # Variable to store the total budget allocated

if sum(budget) >= end:  # If the sum of all budget requests is greater than or equal to the maximum budget request
    print(max(budget))  # Print the maximum budget request
else:
    while start <= end:  # Binary search loop
        mid = (start + end) // 2  # Calculate the middle point

        total_budget = 0  # Reset the total budget allocated

        for i in budget:  # Iterate through each budget request
            total_budget += min(mid, i)  # Allocate the minimum of mid and the budget request

        if total_budget > m:  # If the total allocated budget is greater than the total budget
            end = mid - 1  # Update the end point to search in the lower half
        else:
            start = mid + 1  # Update the start point to search in the upper half

    print(mid)  # Print the maximum budget allocated