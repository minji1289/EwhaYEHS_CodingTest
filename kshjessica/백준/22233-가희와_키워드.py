n, m = map(int, input().split())  # Read the number of keywords and the number of blog posts
keywords = {input().rstrip() for _ in range(n)}  # Create a set of keywords from user input

for _ in range(m):
    for key in input().rstrip().split(','):  # Read the keywords related to each blog post
        keywords.discard(key)  # Remove the keywords from the set

    print(len(keywords))  # Print the number of remaining keywords after each blog post