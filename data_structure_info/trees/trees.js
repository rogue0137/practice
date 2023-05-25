class Node {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
};


const root = Node('a');
const leftNode = Node('b');
const rightNode = Node('c');
root.left = leftNode;
root.right = rightNode;

//    'a'
//    /  \
// 'b'   'c'

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
    // check for root
    if (!root) return root;

    // base case: return root when there are no children 
    if (!root.right || !root.left) {
        return root;
    }

    // recursive case: switch left and right children

    // capture original children
    const originalLeft = root.left;
    const originalRight = root.right;

    // switch values for children
    // switch left to right value
    root.left = originalRight;
    // switch right to left value
    root.right = originalLeft;

    // now see if we need to switch children of the children
    invertTree(root.left);
    invertTree(root.right);

    return root;
};

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
var maxDepth = function(node) {
    // base case
    if (!node) return 0;
    
    // recursive case
    const leftDepth = maxDepth(node.left);
    const rightDepth = maxDepth(node.right);

    return Math.max(leftDepth, rightDepth) + 1;
};
