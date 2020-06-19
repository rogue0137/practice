# Problem Types

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



## Arrays

_arrays_

Basic.

_some examples_

## Breadth First Search (BFS)

_trees and graphs, searching_

compare to DFS

Breadth-first search is an algorithm for traversing tree or graph data structures. It starts at the tree root, and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level 

_some examples_

## Backtracking 

_wtf_ figure out: https://en.wikipedia.org/wiki/Backtracking

Backtracking is a general algorithm for finding all solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate as soon as it determines that the candidate cannot possibly be completed to a valid solution.

## Binary Search

_arrays; used for searching_

In computer science, binary search, also known as half-interval search, logarithmic search, or binary chop, is a search algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array.

## Bit Manipulation

_do this last if time permits_

Bit manipulation is the act of algorithmically manipulating bits or other pieces of data shorter than a word. Computer programming tasks that require bit manipulation include low-level device control, error detection and correction algorithms, data compression, encryption algorithms, and optimization.

## Bucket Sort

_arrays, used for sorting__

Bucket sort, or bin sort, is a sorting algorithm that works by distributing the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively applying the bucket sorting algorithm.

## Depth First Search

_trees and graphs, searching_

compare to BFS

Depth-first search is an algorithm for traversing tree or graph data structures. The algorithm starts at the root node and explores as far as possible along each branch before backtracking.


## Design 

_wtf? like all system design probs? investiage_


## Dynamic Programming

Dynamic Programming is mainly an optimization over plain recursion. Wherever we see a recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming. The idea is to simply store the results of subproblems, so that we do not have to re-compute them when needed later.


## Fast & Slow Pointers

_cyclic linked lists or arrays_

[Fast and slow pointers](https://emre.me/coding-patterns/fast-slow-pointers/)

## Graph

I feel like this includes a bunch of stuff 
[more on graphs](https://www-users.cs.umn.edu/~karypis/parbook/Lectures/AG/chap10_slides.pdf)

## Greedy

A greedy algorithm is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage[1] with the intent of finding a global optimum. In many problems, a greedy strategy does not usually produce an optimal solution, but nonetheless a greedy heuristic may yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time.

For example, a greedy strategy for the travelling salesman problem (which is of a high computational complexity) is the following heuristic: "At each step of the journey, visit the nearest unvisited city." This heuristic does not intend to find a best solution, but it terminates in a reasonable number of steps; finding an optimal solution to such a complex problem typically requires unreasonably many steps. In mathematical optimization, greedy algorithms optimally solve combinatorial problems having the properties of matroids, and give constant-factor approximations to optimization problems with submodular structure.


## Heap

_graphs; binary treets_

In a heap, the highest (or lowest) priority element is always stored at the root. ... Heaps are also crucial in several efficient graph algorithms such as Dijkstra's algorithm. When a heap is a complete binary tree, it has a smallest possible height—a heap with N nodes and for each node a branches always has loga N height.


## In-place reversal of a linked list

_put this under another category; look at your solutions, you've done one_


## Intervals

_trees_

In computer science, an interval tree is a tree data structure to hold intervals. Specifically, it allows one to efficiently find all intervals that overlap with any given interval or point. It is often[citation needed] used for windowing queries, for instance, to find all roads on a computerized map inside a rectangular viewport, or to find all visible elements inside a three-dimensional scene. A similar data structure is the segment tree.

The trivial solution is to visit each interval and test whether it intersects the given point or interval, which requires {\displaystyle O(n)}O(n) time, where {\displaystyle n}n is the number of intervals in the collection. Since a query may return all intervals, for example if the query is a large interval intersecting all intervals in the collection, this is asymptotically optimal; however, we can do better by considering output-sensitive algorithms, where the runtime is expressed in terms of {\displaystyle m}m, the number of intervals produced by the query. Interval trees have a query time of {\displaystyle O(\log n+m)}{\displaystyle O(\log n+m)} and an initial creation time of {\displaystyle O(n\log n)}O(n\log n), while limiting memory consumption to {\displaystyle O(n)}O(n). After creation, interval trees may be dynamic, allowing efficient insertion and deletion of an interval in {\displaystyle O(\log n)}O(\log n) time. If the endpoints of intervals are within a small integer range (e.g., in the range {\displaystyle [1,\ldots ,O(n)]}{\displaystyle [1,\ldots ,O(n)]}), faster and in fact optimal data structures exist[1][2] with preprocessing time {\displaystyle O(n)}O(n) and query time {\displaystyle O(1+m)}{\displaystyle O(1+m)} for reporting {\displaystyle m}m intervals containing a given query point (see[1] for a very simple one).


## Sliding Window

__ get info from here: https://emre.me/coding-patterns/sliding-window/_

## Topological Sort
_graph_

In computer science, a topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.


## Trie

_tree, used for search_

Search Results
Web results

Trie - Wikipediaen.wikipedia.org › wiki › Trie
In computer science, a trie, also called digital tree or prefix tree, is a kind of search tree—an ordered tree data structure used to store a dynamic set or associative array where the keys are usually strings.

## Two Pointers

maybe make a general pointers section??

https://emre.me/coding-patterns/two-pointers/

## Union Find
https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf
