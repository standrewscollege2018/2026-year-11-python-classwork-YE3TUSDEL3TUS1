target=False
scores = []
print("Enter cricket scores one by one (enter 1000 to stop):")
while target==False:
    score = int(input("Enter score: "))
    if score == 1000:
        target=True
        break
    if score < 0:
        print("Score cannot be negative. Try again.")
        continue
    scores.append(score)
count = len(scores)
total_runs = sum(scores)
average_score = total_runs / count if count > 0 else 0
print(f"There were {count} scores entered.")
print(f"The total number of runs is {total_runs} giving an average score of {average_score}")

