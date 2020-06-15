---
#HOW TO RUN: PY HARD


This script is an example of solving the water pouring problem. It is modified from a section of Udacity's [Design of Computer Programs](https://www.udacity.com/course/design-of-computer-programs--cs212) class with Peter Norvig. You can use any three positive numbers. If there is a solution, it will print the steps that get you to that solution. If there is no solution, it will print 'No solution possible'.


##Run this code

Use Python 2.7

Clone this folder using 
```sh
$ git clone https://github.com/rogue0137/practice.git
```

cd into the appropriate folder
```sh
$ cd py_hard
```

Then type
```sh
$ python buckets.py
```

Respond to the input requests. 


##Example with solution
As an example below, I will be using 5, 3, and 4 as our first bucket, second bucket, and desired bucket respectively.

```sh
How many gallons are in your first bucket? 5
How many gallons are in your second bucket? 3
How many gallons are in your desired bucket? 4
```

Because these numbers have a solution, the following will print out:
```sh
Start with 0 gallons in Bucket One and 0 gallons in Bucket Two. All water is in the lake.
Step 1:  Fill bucket one with 5 gallons --> Bucket One has 5 gallons. Bucket Two has 0 gallons.
Step 2:  Pour bucket one into bucket two --> Bucket One has 2 gallons. Bucket Two has 3 gallons.
Step 3:  Empty bucket two --> Bucket One has 2 gallons. Bucket Two has 0 gallons.
Step 4:  Pour bucket one into bucket two --> Bucket One has 0 gallons. Bucket Two has 2 gallons.
Step 5:  Fill bucket one with 5 gallons --> Bucket One has 5 gallons. Bucket Two has 2 gallons.
Step 6:  Pour bucket one into bucket two --> Bucket One has 4 gallons. Bucket Two has 3 gallons.
Solution found.
```

##Example without solution
As an example below, I will be using 552, 45, and 2 as our first bucket, second bucket, and desired bucket respectively.

```sh
How many gallons are in your first bucket? 552
How many gallons are in your second bucket? 45
How many gallons are in your desired bucket? 2
```

Because there is no solution to this problem, the following will print out.
```sh
No solution possible.
```