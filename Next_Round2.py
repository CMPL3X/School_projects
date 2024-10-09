# n - participants
# k - score
# n >= k
# Output - how many participants will advance to the next round.
# 2nd lines value should be > score
# 2nd line - place i-th (no lielaka skaitla uz mazaku)

first_line = input()
second_line = input()

# Split input into lists
first_line_split = first_line.split(" ")
second_line_split = second_line.split(" ")

# Get number of participants and qualifying score
participants = int(first_line_split[0])
qualifying_score = int(first_line_split[1])

# Convert second line to integers
scores = list(map(int, second_line_split))

# Find the k-th place finisher's score
kth_place_score = scores[qualifying_score - 1]

# Count participants who advance
advanced_count = 0
for score in scores:
    if score > 0 and score >= kth_place_score:
        advanced_count += 1

# Print the result
print(advanced_count)