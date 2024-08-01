# Your company built an in-house calendar tool called HiCal. 
# You want to add a feature to see the times in a day when everyone is available.


# GREADY ALGORITHM
def merge_ranges(meetings):
    sorted_meetings = sorted(meetings)
    merged_meetings = []
    
    # question: can we assume there are always at least two meetings? Yes

    first_meeting = sorted_meetings[0]
    first_meeting_start = first_meeting[0]
    first_meeting_end = first_meeting[1] 

    for second_meeting_start, second_meeting_end in sorted_meetings[1:]: 
        # can first_meeting and second_meeting be merged?
        # yes, merge: if the entirety of meeting two is inside meeting_one
        if first_meeting_end > second_meeting_start and first_meeting_end > second_meeting_end:
            continue
        # yes, merge: meeting_one ends after meeting_two starts
        elif first_meeting_end > second_meeting_start:
            first_meeting_end = second_meeting_end
        # yes, merge: if meeting_one ends on the number meeting_two starts on
        elif first_meeting_end == second_meeting_start:
            first_meeting_end = second_meeting_end
        # yes, merge: if both meetinsg start at the same time
        elif first_meeting_start == second_meeting_start:
            new_end = max(first_meeting_end, second_meeting_end)
            first_meeting_end = new_end
        # yes, merge: if both meetings end at the same time:
        elif first_meeting_end == second_meeting_end:
            new_start = min(first_meeting_start, second_meeting_start)
            first_meeting_start = new_start
        # no, append and reset
        else:
            tuple_to_append = (first_meeting_start, first_meeting_end)
            merged_meetings.append(tuple_to_append)
            
            first_meeting_start = second_meeting_start
            first_meeting_end = second_meeting_end
        
    final_tuple = (first_meeting_start, first_meeting_end)
    merged_meetings.append(final_tuple)
    
    return merged_meetings

# This is not the answer provided by interview cake. However, it still passes all the tests.
# I think it is eaiser to understand than the provided solution, BUT it is much more verbose.

# Time Complexity: O(n log n)
# - Any time you sort, it's going to be 0 (n log n)
# - The actual merging is O(n) because we only go through the list once.
# - Since we're taking worst case, we take the larger of the two, so O(n log n)

# Space Complexity: O(n)
# - We're storing the sorted list, so O(n) off the bat
# - At worst, we'd have to store every meeting in the list (if none of them could be merged), so O(n)

# Questions 1: What if we did have an upper bound on the input values? Could we improve our runtime? 
# Would it cost us memory?
# Answer 1: Not worth it. The actual merging process still requires iterating through each meeting, 
# comparing it with others to find overlaps, and then merging them. At best, this is O(n log n) 
# (without additional information or constraints). We already have 0(n log n) for the sort as our original time complexity.
# However, we would increase the space complexity. The given potential solution mentions using buckets. Honestly,
# that code looks more complicated than what I have here. You also create buckets (more memory used) that may have empty spaces.

# Question 2: Could we do this "in place" on the input list and save some space? 
# What are the pros and cons of doing this in place? 
# Answer 2: You could do it in place! It would save on space, but maintain the same Time Complexity. Here's examle code.

def merge_ranges_in_place(meetings):
    # First, sort the meetings in place, w00t! Memory saved!
    meetings.sort()
    
    i = 0  # Index to track the position in the modified list/pointer, very important for this solution
    
    for meeting_index in range(1, len(meetings)):
        # Check if the current meeting overlaps with the next one:

        first_meeting_end = meetings[i][1] 
        second_meeting_start = meetings[meeting_index][0] 
        if first_meeting_end >= second_meeting_start:
            second_meeting_end = meetings[meeting_index][1]
            # Create a new tuple with the merged meeting times
            merged_meeting = (meetings[i][0], max(first_meeting_end, second_meeting_end))
            # Replace the current meeting with the merged one
            meetings[i] = merged_meeting
        else:
            # If there's no overlap, move to the next position in the list
            i += 1
            meetings[i] = meetings[meeting_index]
    
    # Resize the list to remove the unused tail after merging
    # Example of original list: [(1, 3), (2, 4), (5, 7), (6, 8), (9, 10)]
    # Example of list at this point: [(1, 4), (5, 8), (9, 10), (6, 8), (9, 10)]
    # We need to remove (6, 8), (9, 10) from the list, so we use `[i+1:]` since we only need up to [i]
    del meetings[i+1:]
    
    return meetings

# Above also passes test cases when renaming from `merge_ranges_in_place` to `merge_ranges`

