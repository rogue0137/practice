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
 * @return {number[]}
 */
const getLonelyNodes = function(root) {
    const lonelyNodes = [];

    // if a node does not have a sibling, it is lonely
    const hasSibling = (node) => {
        if (!node) return;
        const left = node.left;
        const right = node.right;
        if (left && !right) {
            lonelyNodes.push(left.val)
            hasSibling(left);
        } else if (right && !left) {
            lonelyNodes.push(right.val);
            hasSibling(right);
        } else {
            hasSibling(left);
            hasSibling(right);
        }
    }

    hasSibling(root);

    return lonelyNodes;
    
};
