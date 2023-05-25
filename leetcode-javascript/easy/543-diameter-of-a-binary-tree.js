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
// The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

// The length of a path between two nodes is represented by the number of edges between them.

const diameterOfBinaryTree = function(root) {

    let maxDiameter = 0;
    
    const traverse = (node) => {
        if (!node) return 0;

        const left = traverse(node.left);
        const right = traverse(node.right);

        const leftPlusRight = left + right;
        maxDiameter = Math.max(maxDiameter, leftPlusRight);
        const currDiameter = Math.max(left, right) + 1;

        return currDiameter;

    };

    traverse(root);
    
    return maxDiameter;
};
