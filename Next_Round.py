# n - participants
# k - score
# n >= k
# Output - how many participants will advence to the next round.
# 2nd lines value should be > score
# 2nd line - place i-th (no lielaka skaitla uz mazaku)

first_line = input()

scnd_line = input()

#nosplito vietās kur ir atstarpe
first_line_split = first_line.split(" ")

scnd_line_split = scnd_line.split(" ")

participants = int(first_line_split[0])

score = int(first_line_split[1])

counter = 0

final_counter = 0

while participants > counter :
    participant_score = int(scnd_line_split[counter])
    if participant_score > score :
        final_counter = final_counter + 1
    counter = counter + 1

print(final_counter)