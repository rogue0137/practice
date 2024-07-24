# Your company built an in-house calendar tool called HiCal. 
# You want to add a feature to see the times in a day when everyone is available.

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
