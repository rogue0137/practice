class Solution:
    def numWays(self, posts: int, colors: int) -> int:
        # painting a post 
        # make it different color as i-1th post
        # make it same color as i-1th post (if you are allowed!)
        # you already used one of the k colors, so to get all the other diff colors
        # you need to subtract k from 1
        diff_color = k - 1
        ways = diff_color - same_color

tests = [
    dict(posts=3,colors=2,answer=6)
    # dict(posts=2,colors=1, answer=1)
]

for test in tests:
    solution = Solution()
    assert solution.numWays(test['posts'], test['colors']) == test['answer']