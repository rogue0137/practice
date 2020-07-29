
# Hike, 
# given a map of area
# 2D array of ints
# tell me all the places to get to my 




# flat --> can go to (==) --> true
# uphill --> > cannot go to --> false


# 1 2 1
# 1 2 1 start at (1, 0)
# 1 3 2

# t f f
# t f f
# t f f

# 1 2 1 1 1
# 1 2 1 2 1
# 1 1 1 2 1

# start 1, 2

# t f t t t
# t f t f t
# t t t f t


# visited: 2d boolean array
# toVisit: list of points not yet visited
# start with toVisit = [starting_point]
# For each neighbor of current point, put in toVisit if matrix value is == and is not yet visited

-- PAINT BUCKET PROBLEM
-- NEAREST NEIGHBORS
-- DEPTH FIRST
-- BREADTH FIRST 


def canIgoDown(matrix, starting_point):
    height = len(matrix) # 3
    width = len(matrix[0]) # 3
    # print(f'height: {height}')
    # print(f'width: {width}')
    col = starting_point[0]
    row = starting_point[
    visited_matrix = [[False for _ in range(height)] for _ in range(width)]
    visited_matrix[col][row] = True
    
    to_visit = [staring_point]
    while len(to_visit) != 0:
        current_point = to_visit.pop()
        row = current_point[0]
        col = current_point[1]
        visited_matrix[row][col] = True
        # Visit each of current_point's neighbors
        # go up
        # cover out of index cases
        if visited_matrix[row + 1][col] == matrix[row][col]:
            to_visit.append([row + 1][col])
        # go left
        if matrix[row][col - 1] == matrix[row][col]:
            to_visit.append([row][col - 1])
        # go right
        if visited_matrix[row][col + 1] == matrix[row][col]:
            to_visit.append([row][col + 1])
        # go down
        if visited_matrix[row - 1][col] == matrix[row][col]:
            to_visit.append([row - 1 ][col])