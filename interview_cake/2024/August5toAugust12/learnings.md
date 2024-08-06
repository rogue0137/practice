# Weekly Learnings: August5toAugust12

![husband feeds me while i work](https://media.giphy.com/media/L1R1tvI9svkIWwpVYr/giphy.gif?cid=790b7611aapmshy0toe5i2qtuyunfryjj3k4fvh9vn8g6we8&ep=v1_gifs_search&rid=giphy.gif&ct=g)

## New and Reviewed Weekly Problems

## Tracking Weak Spots

- I keep forgetting that when trying to get the highest number or lowest number AND THEN iterating through the list, I should actually do something like this:
```Python
highest_num = max(list_of_ints[0], list_of_ints[1])
lowest_num = min(list_of_ints[0], list_of_ints[1])
```
- If I start by the above, I can start on index two as current number, knowing that I will have accounted for both of the numbers at indexes before (and properly set `highest_num` and `lowest_num` before reaching current number). Earlier I was struggling to know which index to start at. If I max and min, like above, it's very obvious that I start at index two. It would look like:
```Python
for current_number in list_of_ints[2:]:
    # do the thing
```

## To Do List
- [ ] Solve [product_of_all_other_numbers](product_of_all_other_numbers.py) using division. Watchout for 0s!
- [ ] Solve [inflight_entertainment](inflight_entertainment.py) question #2 using dynamic programming. ( _Carry this TODO over until you get to the dynamic programming section._)

## Patterns

## Learnings
