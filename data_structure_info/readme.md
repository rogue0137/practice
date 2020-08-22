# Problem Types

> The point of this page is to prepare for coding interviews. 

## Overview

- Data Structures
    - [Arrays](https://github.com/rogue0137/practice/blob/master/data_structure_info/arrays/arrays.md) 
    - [Hashmap](https://github.com/rogue0137/practice/tree/master/data_structure_info/hashmap/hashmap.md)
    - Stacks
    - Queues
    - [Linked Lists](https://github.com/rogue0137/practice/blob/master/data_structure_info/linked_lists/linked_lists.md)
    - [Trees](https://github.com/rogue0137/practice/blob/master/data_structure_info/trees/trees.md)
        - Binary Trees and N-ary Trees
        - B-Tree
        - [Heap (a.k.a. Priority Queue)](https://github.com/rogue0137/practice/blob/master/data_structure_info/trees/heap.md)
        - [Trie](https://github.com/rogue0137/practice/blob/master/data_structure_info/trees/trie.md)
    - [Graphs](https://github.com/rogue0137/practice/blob/master/data_structure_info/graphs/graphss.md)
- Algorithms
    - Sliding Window --> arrays
    - Binary Search --> arrays
    - Bucket Sort --> arrays
    - Two pointers --> linked lists
    - Fast and Slow Pointers --> arrays, linked lists
    - Breadth First Search --> trees and graphs
    - Depth First Search --> trees and graphs
    - Topological sort --> graphs
    - Dynamic Programming
    - Greedy

## Data Structures: Diagram
![Data Structures](images/data_structures.jpg)


## Algorithms


### Sliding Window

__ get info from here: https://emre.me/coding-patterns/sliding-window/

### Binary Search

_arrays; used for searching_

In computer science, binary search, also known as half-interval search, logarithmic search, or binary chop, is a search algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array.

### Bucket Sort

_arrays, used for sorting__

Bucket sort, or bin sort, is a sorting algorithm that works by distributing the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting algorithm.

### Two Pointers

maybe make a general pointers section??

https://emre.me/coding-patterns/two-pointers/

### Fast & Slow Pointers

_cyclic linked lists or arrays_

[Fast and slow pointers](https://emre.me/coding-patterns/fast-slow-pointers/)


### In-place reversal of a linked list

_put this under another category??? look at your solutions, you've done one_



### Breadth First Search (BFS)

_trees and graphs, searching_

compare to DFS

Breadth-first search is an algorithm for traversing tree or graph data structures. It starts at the tree root, and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level 

_some examples_


### Depth First Search

_trees and graphs, searching_

compare to BFS

Depth-first search is an algorithm for traversing tree or graph data structures. The algorithm starts at the root node and explores as far as possible along each branch before backtracking.

## Topological Sort
_graph_

In computer science, a topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.

### Dynamic Programming

Dynamic Programming is mainly an optimization over plain recursion. Wherever we see a recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming. The idea is to simply store the results of subproblems, so that we do not have to re-compute them when needed later.


## Greedy

A greedy algorithm is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage[1] with the intent of finding a global optimum. In many problems, a greedy strategy does not usually produce an optimal solution, but nonetheless a greedy heuristic may yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time.

For example, a greedy strategy for the travelling salesman problem (which is of a high computational complexity) is the following heuristic: "At each step of the journey, visit the nearest unvisited city." This heuristic does not intend to find a best solution, but it terminates in a reasonable number of steps; finding an optimal solution to such a complex problem typically requires unreasonably many steps. In mathematical optimization, greedy algorithms optimally solve combinatorial problems having the properties of matroids, and give constant-factor approximations to optimization problems with submodular structure.




The problem types below are taken from [Leetcode Patterns](https://seanprashad.com/leetcode-patterns/). Many of the defitions below are modified from [Wikipedia](https://en.wikipedia.org/) definitions. Each type includes (or will include) a link to a finished python solution.

1. Arrays
2. BFS
3. Backtracking
4. Binary Search
5. Bit Manipulation
6. Bucket Sort
7. DFS
8. Design
9. Dynamic Programming
10. Fast & Slow Pointers
11. Graph
12. Greedy
13. Heap
14. In-place reversal of a linked list
15. Intervals
16. Sliding Window
17. Topological Sort
18. Trie
19. Two Pointers
20. Union Find


_figure out where to put these__

## Backtracking 

_wtf_ figure out: https://en.wikipedia.org/wiki/Backtracking

Backtracking is a general algorithm for finding all solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate as soon as it determines that the candidate cannot possibly be completed to a valid solution.


## Bit Manipulation

_do this last if time permits_

Bit manipulation is the act of algorithmically manipulating bits or other pieces of data shorter than a word. Computer programming tasks that require bit manipulation include low-level device control, error detection and correction algorithms, data compression, encryption algorithms, and optimization.


## Design 

_wtf? like all system design probs? investiage_






## Union Find
https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf
