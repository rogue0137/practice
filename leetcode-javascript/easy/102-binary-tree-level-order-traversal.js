/**
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

    const queue = [root];
    const levelOrderTraversal = [];

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
