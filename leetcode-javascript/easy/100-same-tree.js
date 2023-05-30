/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
const isSameTree = function(treeOneNode, treeTwoNode) {
    // 3 False Cases; 2 True Cases

    // True 1: if treeOneNode does not exist AND treeTwoNode does not exist
    if (treeOneNode === null && treeTwoNode === null) {
        return true;
    }

    // False 2: if treeOneNode exists, BUT treeTwoNode does not exist
    if (treeOneNode !== null && treeTwoNode === null) {
        return false;
    }
    // False 3: if treeOneNode does not exist, BUT treeTwoNode does exist
    if (treeOneNode === null && treeTwoNode !== null) {
        return false;
    }

    // True 2: if treeOneNode.val AND treeTwoNode.val are the same 
    // RECURSIVE CASE traverse left and right side of traverse
    if (treeOneNode.val === treeTwoNode.val) {
        const leftSide = isSameTree(treeOneNode.left, treeTwoNode.left);
        const rightSide = isSameTree(treeOneNode.right, treeTwoNode.right);
        return leftSide && rightSide;
    }
    
    // False 1: if treeOneNode.val AND treeTwoNode.val are DIFFERENT
    if (treeOneNode.val !== treeTwoNode.val ) {
        return false;
    }
};
