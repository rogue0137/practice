/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */

/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */

// For a Binary Search tree, you can assume the leftmost number 
// is the smallest and the rightmost number is the largest.
// In a binary search tree, all nodes on the left are smaller than the root,
// and all nodes on the right are larger than the root.
const lowestCommonAncestorRecursive = function(root, p, q) {
    // if both P and Q are in the left subtree
    if (p.val < root.val && q.val < root.val) {
        return lowestCommonAncestor(root.left, p, q);
    }

    // if both P and Q are in the right subtree
    if (p.val > root.val && q.val > root.val) {
        return lowestCommonAncestor(root.right, p, q);
    }

    // if P is in one subtree and Q is in the other subtree
    return root;
};

const lowestCommonAncestorIterative = function(root, p, q) {
    while (root) {
        // if both P and Q are in the left subtree
        if (p.val < root.val && q.val < root.val) {
            root = root.left;
        // if both P and Q are in the right subtree
        } else if (p.val > root.val && q.val > root.val) {
            root = root.right
        // if P is in one subtree and Q is in the other subtree
        } else {
        return root;
        }
    }
    return null;
};
