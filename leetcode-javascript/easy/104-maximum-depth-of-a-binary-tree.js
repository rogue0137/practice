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
 * @return {number}
 */
var maxDepthRecursive = function(node) {

    if (!node ) return 0;

    const leftDepth = maxDepthRecursive(node.left);
    const rightDepth = maxDepthRecursive(node.right);

    const maxDepth = Math.max(leftDepth, rightDepth);
    const currentDepth = maxDepth + 1;

    return currentDepth;
};

const maxDepthIterative = (root) => {
    if (!root) return 0;

    let queue = [root]; // 1. [node of 3]
    let depth = 0;

    while (queue.length) { 
        // this queue.length, then using it in a for...loop
        // is a pattern; see 102 for another example
        let size = queue.length; 

        for (let i = 0; i < size; i++) { 
            let node = queue.shift();

            if (node.left) queue.push(node.left); 
            if (node.right) queue.push(node.right); 
        }

        depth++; 
    }

    return depth;
};

