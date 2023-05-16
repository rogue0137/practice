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
var maxDepthRecursive = function(node) {

    if (!node ) return 0;

    // Memorize this pattern! A lot of other exercises use this pattern
    return Math.max(maxDepth(node.right), maxDepth(node.left)) + 1;
};

const maxDepthIterative = (root) => {
    if (!root) return 0;

    let queue = [root];
    let depth = 0;

    while (queue.length) {
        // this queue.length, then using it in a for...loop
        // is a pattern; see 102 for another example
        let size = queue.length;

        for (let i = 0; i < size; i++) {
            let node = queue.shift();

            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }

        depth++;
    }

    return depth;
};

