# You created a game that is more popular than Angry Birds.

# Each round, players receive a score between 0 and 100, which you use to rank them from highest to lowest. So far you're using an algorithm that sorts in 
# O(N log N) time, but players are complaining that their rankings aren't updated fast enough. You need a faster sorting algorithm.

# Write a function that takes:
# - a list of unsorted_scores
# - the highest_possible_score in the game
# and returns a sorted list of scores in less than O(N log N) time.

def sort_scores(unsorted_scores, highest_possible_score):

    score_counts = [0] * highest_possible_score
    
    for score in unsorted_scores:
        score_counts[score] += 1
    
    all_scores = []
    
    # The index represents a potential score
    # The count at the index indicates how many people got that score
    # We're iterating backwards because we want the scores to be in order from
    #   highest to lowest. If we wanted lowest to highest, we'd instead do
    #   for index in range(len(score_counts)):
    for index in range(len(score_counts) - 1, -1, -1):
        counts = score_counts[index]
        if counts != 0:
            for count in range(counts):
                all_scores.append(index)

    return all_scores

# TIME COMPLEXITY: O(N) because we have to iterate through each score unsorted_score. (If we're not looking at
# highest_possible_score as a constant, it'd be 0 (N + K))

# SPACE COMPLEXITY: O(K) because we are dependent on the highest score. But if you're still ignoring K as a constant
# you'd say O(N) because you have to iterate through all of unsorted_scores.

# NOTE: I should have probably named `all_scores` something like `scores_sorted_from_highest_to_lowest`

# QUESTION 1: Note that by optimizing for time we ended up incurring some space cost! What if we were optimizing for space?
# Answer: We'd incure more time cost. Here's an example solution that saves space at exactly O(N), but brings our time complexity
# up to O (N log N).

def sort_scores_space_optimized(unsorted_scores):
    score_counts = {}
    for score in unsorted_scores:
        if score in score_counts:
            score_counts[score] += 1
        else:
            score_counts[score] = 1
    
    # Sorting the keys (scores) will take O(n log n) time
    sorted_scores = sorted(score_counts.keys(), reverse=True)
    
    all_scores = []
    for score in sorted_scores:
        all_scores.extend([score] * score_counts[score])
    
    return all_scores
