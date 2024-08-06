# See interview_cake/2024/July29toAugust2/inflight_entertainment.py
# for actual code answer to original.

# QUESTION 1: What if we wanted the movie lengths to sum to something close to the flight length (say, within 20 minutes)?
# ANSWER: This finds one pair.
def can_two_movies_fill_flight(movie_lengths, flight_length):
    movie_lengths_set = set(movie_lengths)

    for first_movie_length in movie_lengths:
        # Calculate the range for the second movie length considering the tolerance
        # 20 min under exact time
        under_twenty = flight_length - first_movie_length - 20
        min_target_length = max(0, under_twenty )
        # 20 min over exact time
        max_target_length = flight_length - first_movie_length + 20

        # Check if there exists a movie within the acceptable range
        for potential_second_movie_length in range(min_target_length, max_target_length + 1):
            if potential_second_movie_length != first_movie_length and potential_second_movie_length in movie_lengths_set:
                return True

    return False



# ANSWER: This finds all pairs using pointers.
def find_movie_pairs(movie_lengths, flight_length):
    # Sort the movie lengths
    movie_lengths.sort()
    
    # List to store the pairs of movies
    pairs = []
    
    # Initialize two pointers
    left, right = 0, len(movie_lengths) - 1
    
    while left < right:
        current_sum = movie_lengths[left] + movie_lengths[right]
        
        # Check if the current sum is within the acceptable range
        if abs(current_sum - flight_length) <= 20:
            # Ensure the pair is added only once by ordering the lengths
            sorted_pair = tuple(sorted([movie_lengths[left], movie_lengths[right]]))
            
            # Add the pair if it's not already in the pairs list
            if sorted_pair not in pairs:
                pairs.append(sorted_pair)
            
            # Move both pointers towards the center
            left += 1
            right -= 1
        elif current_sum < flight_length:
            # If the sum is too small, move the left pointer to increase the sum
            left += 1
        else:
            # If the sum is too large, move the right pointer to decrease the sum
            right -= 1
    
    return pairs




# QUESTION 2: What if we wanted to fill the flight length as nicely as possible with any number of movies (not just 2)?
# NOTE: Will do with the dynamic programming chapter.

# QUESTION 3: What if we knew that movie_lengths was sorted? Could we save some space and/or time?
# ANSWER: If it's already sorted, you can use the pointer approach above to save space (no need to create a set!).


def can_two_movies_fill_flight_already_sorted(movie_lengths, flight_length):
    left, right = 0, len(movie_lengths) - 1
    
    while left < right:
        current_sum = movie_lengths[left] + movie_lengths[right]
        
        if current_sum == flight_length:
            return True
        elif current_sum < flight_length:
            left += 1  # Move left pointer to increase the sum
        else:
            right -= 1  # Move right pointer to decrease the sum
    
    return False
