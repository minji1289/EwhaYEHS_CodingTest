# Read the number of keywords and the number of blog posts
n, m = map(int, input().split())
# Create a set of keywords from user input
keywords = {input().rstrip() for _ in range(n)}

for _ in range(m):
    # Read the keywords related to each blog post
    for key in input().rstrip().split(','):
        # Remove the keywords from the set
        keywords.discard(key)

    # Print the number of remaining keywords after each blog post
    print(len(keywords))