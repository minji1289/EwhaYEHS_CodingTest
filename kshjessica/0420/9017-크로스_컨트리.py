t = int(input())  # Number of test cases

for i in range(t):
    n = int(input())  # Number of participants
    team = list(map(int, input().strip().split()))  # List of team numbers

    team_info = {}  # Dictionary to store team information
    rank = 1  # Initialize rank
    result = []  # List to store results
    
    # Count the number of participants in each team
    for j in range(n):
        if team[j] not in team_info:
            team_info[team[j]] = [1, [], 0]
        else:
            team_info[team[j]][0] += 1

    excluded_teams = set(k for k, v in team_info.items() if v[0] < 6)  # Set of teams with less than 6 participants

    # Calculate rank and total score for each team
    for j in range(n):
        if team[j] not in excluded_teams:
            team_info[team[j]][1].append(rank)

            if len(team_info[team[j]][1]) <= 4: 
                team_info[team[j]][2] += rank
            rank += 1

    # Create a list of teams with their fifth participant's rank and total score
    for k, v in team_info.items():
        if len(v[1]) != 0 and v[2] != 0:
            result.append([k, v[1][4], v[2]])

    # Sort the result list based on total score and fifth participant's rank
    sorted_result = sorted(result, key=lambda x: (x[2], x[1]))
    
    print(sorted_result[0][0])  # Print the team number of the winning team