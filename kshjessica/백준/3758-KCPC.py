# test case count
T = int(input())

for _ in range(T):
    # number of teams, problems, team ID, log entries
    n, k, t, m = map(int, input().split())
    
    # initialize scores, times, and attempts lists
    scores = [[0]*(k+1) for _ in range(n+1)]
    times = [0]*(n+1)
    attempts = [0]*(n+1)
    
    # Log entries
    for time in range(1, m+1):
		    # team ID, problem ID, score
        i, j, s = map(int, input().split())
        # update the maximum score for the team and problem
        scores[i][j] = max(scores[i][j], s)
        # record the last submission time for the team
        times[i] = time
        # increment the number of attempts for the team
        attempts[i] += 1

    # calculate final scores and sort teams
    final_scores = [(sum(scores[i]), -attempts[i], -times[i], i) for i in range(1, n+1)]
    final_scores.sort(reverse=True)

    # find and print the rank of team t
    print([i for _, _, _, i in final_scores].index(t) + 1)
