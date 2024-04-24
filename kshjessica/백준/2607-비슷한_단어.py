# Number of words given
n = int(input())
# First word to compare against
target = list(input())
# Counter for similar words
answer = 0

for _ in range(n - 1):
    compare = target[:]  # Make a copy of the target word
    word = input()  # Get the next word to compare
    cnt = 0  # Counter for differences between words

    for w in word:
        if w in compare:
            # Remove matching characters from the copy
            compare.remove(w)
        else:
            # Increment the difference counter
            cnt += 1

            

    if cnt < 2 and len(compare) < 2:
        answer += 1 

# Print the number of similar words
print(answer)