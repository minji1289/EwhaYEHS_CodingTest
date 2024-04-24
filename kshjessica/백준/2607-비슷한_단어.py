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
            cnt += 1  # Increment the difference counter

    if cnt < 2 and len(compare) < 2:
        answer += 1  # Increment the answer counter if the words are similar

# Print the number of similar words
print(answer)