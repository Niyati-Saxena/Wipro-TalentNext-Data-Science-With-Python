# Given a list of scores from a university sports day, find the runner-up score. Store them in list and find score of runner-up.

scores = list(map(int, input("Enter scores separated by space: ").split()))
unique_scores = list(set(scores))
unique_scores.sort(reverse=True)
runner_up = unique_scores[1]
print("Runner-up score:", runner_up)
