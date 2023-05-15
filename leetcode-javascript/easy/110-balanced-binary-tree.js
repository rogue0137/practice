// A height-balanced binary tree is a binary tree in which 
// the depth of the two subtrees of every node never differs by more than one.
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
 * @return {boolean}
 */
const isBalanced = function(root) {
    let balancedBoolean = true;

    const traverse = function(node) {
        if (!node) return 0;

        const leftHeight = traverse(node.left);
        const rightHeight = traverse(node.right);

        if (Math.abs(leftHeight - rightHeight) > 1) {
            balancedBoolean = false;
        } 

        return Math.max(leftHeight, rightHeight) + 1;

    };
    
    traverse(root);

    return balancedBoolean;
};
