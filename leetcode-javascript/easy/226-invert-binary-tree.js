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
 * @return {TreeNode}
 */
const invertTree = function(root) {
    // BFS => uses queue for iterative 
    if (!root) return root;

    const queue = [];
    queue.push(root);

    while (queue.length > 0) {
        let curr = queue.shift();
        let left = curr.left;
        let right = curr.right;
        curr.left = right;
        curr.right = left;
        if (curr.left) queue.push(curr.left);
        if (curr.right) queue.push(curr.right);
    }
    return root
};

// Add recursive solution
// Add DFS solution
