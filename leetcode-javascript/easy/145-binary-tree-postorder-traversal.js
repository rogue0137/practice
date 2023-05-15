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

    const getNodevalue = ( node ) => {
        if (!node) return;
        getNodevalue(node.left);
        getNodevalue(node.right);
        treeOrder.push(node.val);
    }
    getNodevalue(root);
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
