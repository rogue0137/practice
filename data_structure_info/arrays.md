# Arrays

## Valid Subsequence

[Algo Expert Valid Subsequence](https://www.algoexpert.io/questions/Validate%20Subsequence)

_Two pointers approach_
1. You will have to iterate through both the array and seq, each with their own pointer
    - arr_idx
    - seq_idx
2. Once you are at the end of either, you can check the seq len
3. If seq_idx equals sequence length, then you have confirmed that each item in the sequence was found in order

Notes:
- Regardless of a match, you will always move the array pointer forward

```python
def isValidSubsequence(array, sequence):
    arr_idx = 0
    seq_idx = 0
    
    while seq_idx < len(sequence) and arr_idx < len(array):
        arr_num = array[arr_idx]
        seq_num = sequence[seq_idx]
        
        if arr_num == seq_num:
            seq_idx += 1
        
        arr_idx += 1
    
    return seq_idx == len(sequence)
```

## Three sum

[AlgoExpert Three-Sum](https://www.algoexpert.io/questions/Three%20Number%20Sum)

_Two Pointers Approach_
0. If not already sorted, you MUST sort the array
1. Iterate through the original array
2. At each spot in the array, use a L and R pointers
    - L is for left pointer, it should always be one ahead of current index
    - R is for right pointer, it should always start at the last index and work its way towards the L pointer
    - L should always be less than R
    - R should always be more than L
3. Create a while lop that will check for the specified cases above
4. Find the numbers at each index
5. Calculate the sum, here total_sum
6. compare total_sum to target_sum
    - Move L pointer one up less than target_sum
    - Move R pointer one down if greater than target_sum


Note:
- `while L < R` is a common pattern for these type of problems

```python
# array = [12, 3, 1, 2, -6, 5, -8, 6]
# targetSum = 0
# output = [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

def threeNumberSum(array, targetSum):
    sorted_array = sorted(array)
    three_num_sum = []

    for idx, num in enumerate(sorted_array):
        L = idx + 1
        R = len(sorted_array) - 1
        while L < R:
            second_num = sorted_array[L]
            third_num = sorted_array[R]
            total_sum = num + second_num + third_num
            if total_sum > targetSum:
                R -= 1 
            if total_sum < targetSum:
                L += 1 
            if total_sum == targetSum:
                three_num_sum.append([num, second_num, third_num])
                R -= 1
                L += 1
            
    return three_num_sum
```