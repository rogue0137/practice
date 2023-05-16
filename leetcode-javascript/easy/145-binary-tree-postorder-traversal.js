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
/// RECURSIVE SOLUTION
const postorderRecursiveTraversal = function(root) {
    const treeOrder = [];

    const getNodeValue = ( node ) => {
        if (!node) return;
        getNodeValue(node.left);
        getNodeValue(node.right);
        treeOrder.push(node.val);
    }
    getNodeValue(root);
    return treeOrder; 
};

// ITERATIVE SOLUTION
// DFS => uses stack for iterative
const postorderIterativeTraversal = function(root) {
    if(!root) return [];
    
    const stack = [root];
    const treeOrder = [];

    while (stack.length) {
        const node = stack.pop();
        treeOrder.unshift(node.val);
        if (node.left) stack.push(node.left);
        if (node.right) stack.push(node.right);
    }

    return treeOrder;
}
