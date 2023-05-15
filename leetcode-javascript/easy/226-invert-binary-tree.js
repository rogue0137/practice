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
const invertTreeIterativeBFS = function(root) {
    // BFS => uses queue for iterative 
    if (!root) return root;

    const queue = [root];

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
const invertTreeRecursive = function(root) {
    if (!root) return root;
    let left = root.left;
    let right = root.right;
    root.left = invertTreeRecursive(right);
    root.right = invertTreeRecursive(left);
    return root;
};

// Add DFS solution
const invertTreeIterativeDFS = function(root) {
    // DFS => uses stack for iterative 
    if (!root) return root;

    const stack = [root];

    while (stack.length) {
        let curr = stack.pop();
        let left = curr.left;
        let right = curr.right;
        curr.left = right;
        curr.right = left;
        if (curr.left) stack.push(curr.left);
        if (curr.right) stack.push(curr.right);
    }
    return root
};
