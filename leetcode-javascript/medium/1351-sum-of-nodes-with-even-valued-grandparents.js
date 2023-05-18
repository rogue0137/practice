/**
 * https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/
 * 
 * Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. 
 * If there are no nodes with an even-valued grandparent, return 0.
 * 
 * Example 1:
 * Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
 * Output: 18
 * 
 * Example 2:
 * Input: root = [1]
 * Output: 0
 * 
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */


// Using a tuple is not very memory efficient;
// see sumEvenGrandparentWhileForLoops for a more memory efficient solution.

var sumEvenGrandparentTuple = function(root) {
    const grandchildren = [];

    const stack = [];
    const firstTuple = [root, null, null];
    stack.push(firstTuple);

    while (stack.length) {
        const fakeTuple = stack.pop();
        const node = fakeTuple[0];
        const parent = fakeTuple[1];
        const grandparent = fakeTuple[2];

        if (grandparent !== null && grandparent % 2 === 0) {
            grandchildren.push(node.val)
        }

        if (node.left) {
            stack.push( [node.left, node.val, parent] )
        }
                
        if (node.right) {
            stack.push( [node.right, node.val, parent])
        }

    }

    const granchildren_sum = grandchildren.reduce((grandchild, nextGrandchild) => grandchild + nextGrandchild, 0);
    return granchildren_sum;
    
    
};

var sumEvenGrandparentWhileForLoops = function(root) {
    const grandchildren = [];

    // write the rest

    const granchildren_sum = grandchildren.reduce((grandchild, nextGrandchild) => grandchild + nextGrandchild, 0);
    return granchildren_sum;
    
    
};
