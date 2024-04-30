N = int(input())  # Number of cities
distances = list(map(int, input().split()))  # Distances between cities
prices = list(map(int, input().split()))  # Prices of fuel in each city

total_cost = 0  # Total cost of fuel
min_price = prices[0]  # Initialize the minimum price with the first city's price

for i in range(N-1):
    # Update the minimum price if a lower price is found
    if prices[i] < min_price:
        min_price = prices[i]
    
    # Calculate the cost of fuel for the current distance
    cost = min_price * distances[i]
    
    # Add the cost to the total cost
    total_cost += cost

print(total_cost)