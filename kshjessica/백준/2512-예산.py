# Number of regions
n = int(input())
# Budget requests for each region
budget = list(map(int, input().split()))
# Total budget
m = int(input())
# Initialize start and end points for binary search
start, end = 0, max(budget) 
# Variable to store the total budget allocated
total_budget = 0 

# If the sum of all budget requests is greater than or equal to the maximum budget request
if sum(budget) >= end:
    # Print the maximum budget request 
    print(max(budget))
else:
    # Binary search loop
    while start <= end:
        # Calculate the middle point
        mid = (start + end) // 2

        # Reset the total budget allocated
        total_budget = 0 

        for i in budget:  # Iterate through each budget request
            total_budget += min(mid, i)  # Allocate the minimum of mid and the budget request

        if total_budget > m:  # If the total allocated budget is greater than the total budget
            end = mid - 1  # Update the end point to search in the lower half
        else:
            start = mid + 1  # Update the start point to search in the upper half

    print(mid)  # Print the maximum budget allocated