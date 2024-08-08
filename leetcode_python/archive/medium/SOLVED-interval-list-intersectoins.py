# 986. Interval List Intersections
# https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(
        self,
        A: List[List[int]], 
        B: List[List[int]]) -> List[List[int]]:
    # two lists of lists
    # len of A
        lenA = len(A)
        # len of B
        lenB = len(B)
        idx_of_A = 0
        # p2 = 4
        idx_of_B = 0

        # overlaps
        overlap = []
        # where is the first overlap?
        # where does that overlap end?

        # while p1 < len of A and p2 < len of B 
        while idx_of_A < lenA and idx_of_B < lenB:
            startA, endA = A[idx_of_A]
            startB, endB = B[idx_of_B]
            curr_start = max(startA, startB)
            curr_end = min(endA, endB)
            # curr_start vs. curr_end
            if curr_start <= curr_end:
                interval = [curr_start, curr_end]
                overlap.append(interval)
            # verify which end is less
            # move that end over one
            if endA < endB:
                idx_of_A += 1
            else:
                idx_of_B += 1

        return overlap

# Runtime: 156 ms, faster than 88.04% of Python3 online submissions for Interval List Intersections.
# Memory Usage: 14.3 MB, less than 90.00% of Python3 online submissions for Interval List Intersections.
        # start
        # ROUND 1
            # 0 -> startA, endA = 3, 5
            # 0 -> startB, endB = 4, 5
            # startB greater: 4
            # endA greater: 5
            # add [4, 5]
            # move A
        # ROUND 2
            # 1 -> startA, endA = 9, 20
            # 0 -> startB, endB = 4, 5
            # startA greater: 9
            # endB less: 5
            # no overlap, move B
        # ROUND 3
            # 1 -> startA, endA = 9, 20
            # 2 -> startB, endA = 7, 10
            # startA greater: 9
            # endB greater: 10
            # add [9, 10]
            # move over B
        # ROUND 4
            # 1 -> startA, endA = 9, 20
            # 2 -> startB, endB = 11, 12
            # startB greater: 11
            # endA greater: 20
            #

        # start
        # ROUND 1 --> DONE
            # A -> P1 = 0 => 0, 2
            # B -> P2 = 0 => 1, 5
            # 0 < 1
                # B is bigger
                # 1 is start
                # look at A end
            # 1 < 2
                # A end is bigger than B start
                # 1 is start
                # 2 is end
            # add 1, 2
            # move A over one
        # ROUND 2 --> done
            # A -> P1 = 1 => 5, 10
            # B -> P2 = 0 => 1, 5
            # 5 > 1
                # A is bigger
                # 5 is start
                # look at B end
            # 5 = 5
                # they are equal
                # add 5, 5
                # move B over 1
        # ROUND 3 --> DONE
            # A -> P1 = 1 => 5, 10
            # B -> P2 = 1 => 8, 12
            # 5 < 8
                # B is bigger
                # 8 is start
                # look at A for end
            # 8 < 10
                # A is bigger
                # add 8, 10
                # move A over one
        # ROUND 4
            # A -> P1 = 2 => 13, 23
            # B -> P2 = 1 => 8, 12
            # 13 > 8
                # A is bigger
                # 13 is start
                # look at B end
            # 13 > 12
                # start is before end
                # continue, no add
                # move B over 1
        # ROUND 5
            # A -> P1 = 2 => 13, 23
            # B -> P2 = 2 => 15, 24
            # 13 < 15
                # B is bigger
                # start is 15
                # look at A end
            # 13 < 23
                # A is bigger
                # add 13, 23
                # move A over one
        # ROUND 6
            # A -> P1 = 3 => 24, 25
            # B -> P2 = 2 => 15, 24
            # 24 > 15
                # A is bigger
                # start is 24
                # look at end B
            # 24 = 24
                # they are the same
                # add 24, 24
                # move B over 1
        # ROUND 7
            # A -> P1 = 3 => 24, 25
            # B -> P2 = 3 => 25, 26
            # 24 < 25
                # B is larger
                # 25 is start
                # look at A end
            # 25 = 25
                # they are the same
                # add 25, 25
                # move A over 1
                # finish while loop
        # [[1,2],[5,5],[8,10],[13,23],[24, 24],[25, 25]]