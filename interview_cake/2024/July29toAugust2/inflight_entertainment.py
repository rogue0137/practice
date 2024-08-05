# You've built an inflight entertainment system with on-demand movie streaming.

# Users on longer flights like to start a second movie right when their first 
# one ends, but they complain that the plane usually lands before they can see 
# the ending. So you're building a feature for choosing two movies whose total 
# runtimes will equal the exact flight length.

# Write a function that takes an integer flight_length (in minutes) and a list of 
# integers movie_lengths (in minutes) and returns a boolean indicating whether there 
# are two numbers in movie_lengths whose sum equals flight_length.


# When building your function:

# 1. Assume your users will watch exactly two movies
# 2. Don't make your users watch the same movie twice
# 3. Optimize for runtime over memory

# SOLUTION 1: LESS SPACE SOLUTION, BUT 0(N^2) TIME AT WORST, SO CAN NOT USE IN AN INTERVIEW
def can_two_movies_fill_flight(movie_lengths, flight_length):

    if len(movie_lengths) == 0 or len(movie_lengths) == 1:
        return False
        
    for index, movie in enumerate(movie_lengths):
        second_movie = flight_length - movie
        if second_movie in movie_lengths:
            if movie == second_movie:
                count_of_movies_this_length = movie_lengths.count(second_movie)
                if count_of_movies_this_length < 2:
                    continue
            return True
    
    return False

# SOLUTION 2: MORE SPACE, BUT USING A SET, SO O(N) COMPLEXITY
def can_two_movies_fill_flight(movie_lengths, flight_length):

    movie_lengths_seen = set()

    for first_movie_length in movie_lengths:
        second_movie_length = flight_length - first_movie_length
        if second_movie_length in movie_lengths_seen:
            return True
        movie_lengths_seen.add(first_movie_length)


    return False



# QUESTION 1: What if we wanted the movie lengths to sum to something close to the flight length (say, within 20 minutes)?
# ANSWER: This brings up more questions. Do we want to find the first two numbers that are within 20 minutes? 
# Do we want all pairs? What is our output? That will define how the function changes.

# QUESTION 2: What if we wanted to fill the flight length as nicely as possible with any number of movies (not just 2)?
# ANSWER: Same as above, more questions! Do we want to put in as many movies as possible? Give a list of options?

# QUESTION 3: What if we knew that movie_lengths was sorted? Could we save some space and/or time?
