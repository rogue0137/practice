/**
 * https://leetcode.com/problems/binary-tree-level-order-traversal/
 * 
 * Given the root of a binary tree, return the level order traversal of its nodes' values. 
 * (i.e., from left to right, level by level).
 * 
 * Example 1:
 * Input: root = [3,9,20,null,null,15,7]
 * Output: [[3],[9,20],[15,7]]
 * 
 * Example 2:
 * Input: root = [1]
 *  Output: [[1]]
 * 
 * Example 3:
 * Input: root = []
 * Output: []
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
 * @return {number[][]}
 */

 // BFS uses queue
const levelOrder = function(root) {
    if (!root) return [];

    // We are using the queue to store the nodes.
    // As we evaluate them, they are removed from the queue
    // and their children are added to the queue.
    // The queue ensures we evaluate all nodes level by level.
    const queue = [root];
    const levelOrderTraversal = [];

    /*  
    Pattern:
    while (queue.length) {
        ...
        const currentLength = queue.length;
        for (let i = 0; i < currentLength; i++) {
            ...
        }
    }
    See 104 for another example.
    */
   
    while (queue.length) {

        // this queue.length, then using it in a for...loop
        // is a pattern; see 104 for another example
        const currentLength = queue.length;
        const currLevel = [];

        // need to be able to delete from front of queue
        for (let i = 0; i < currentLength; i++) {
            const node = queue.shift();
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
            currLevel.push(node.val);
        }
        levelOrderTraversal.push(currLevel);
    }

    return levelOrderTraversal;    
};
