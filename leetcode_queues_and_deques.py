# https://leetcode.com/problems/moving-average-from-data-stream/
from collections import deque 

size = 3
ints_to_queue = [1, 10, 3, 5]

# create queue
queue = deque(maxlen=size)

# iterate through process
for i in ints_to_queue:
	print('i = {}'.format(i))
	queue.append(i)
	print('sum = {}'.format(sum(queue)))
	print('len of queue = {}'.format(len(queue)))
	print('sum / len = {}'.format(sum(queue)/len(queue)))