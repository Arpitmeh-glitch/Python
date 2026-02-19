N = int(input("Enter number of students: "))
scores = list(map(int, input("Enter scores: ").split()))
unique_scores = list(set(scores))
unique_scores.sort()
runner_up = unique_scores[-2]
print("Runner-up score is:", runner_up)