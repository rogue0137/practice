# HEAP, a.k.a. Priority Queue

## Basics

Heap/Priority Queue
- a type of tree
- called a "heap" because it satisfies the _heap property_, where each node in a tree has a value which is more extreme (greater or less) than or equal to the value of its parent
- min-heap: parent value will always be less than or equal to child key (aka, value)
- max-heap: parent value will alawys be greater than or equal to child key (aka, value)
- binary-heap: a binary tree which satisfies the heap property
- used in Dijkstra's algorithm, which is basically find the shortest path between two nodes

Heap Operations:
    - create
    - delete
    - find_max/find_min (peek, like pop w/out removing item)
    - insert (push)
    - get_max/get_min (pop)
    - delete_max/delet_min
    - replace ???
    - heapify: creating a heapy from anarray
    - merge (union): joining two heaps to form a valid new heap containing all the elements of both, preserving the original heaps.
    - meld: joining two heaps to form a valid new heap containing all the elements of both, destroying the original heaps
    - size
    - is-empty
    - increase-key/decrease-key: basically, updating the value of a key
    - delete
    - sift-up/sift-down: move node up/down tree