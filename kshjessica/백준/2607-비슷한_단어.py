n = int(input())  # Number of words given
target = list(input())  # First word to compare against
answer = 0  # Counter for similar words

for _ in range(n - 1):
    compare = target[:]  # Make a copy of the target word
    word = input()  # Get the next word to compare
    cnt = 0  # Counter for differences between words

    for w in word:
        if w in compare:
            compare.remove(w)  # Remove matching characters from the copy
        else:
            cnt += 1  # Increment the difference counter

    if cnt < 2 and len(compare) < 2:
        answer += 1  # Increment the answer counter if the words are similar

print(answer)  # Print the number of similar words