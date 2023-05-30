/**
 * https://leetcode.com/problems/symmetric-tree/description/
 * 
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
const isSameTree = (treeOne, treeTwo) => {
    // 3 False cases & 2 true cases for Same Tree
    
    // TRUE 1   
    if (treeOne === null && treeTwo === null) {
        return true;
    }

    // FALSE 1
    if (treeOne === null && treeTwo !== null) {
        return false;
    }

    // FALSE 2
    if (treeOne !== null && treeTwo === null ) {
        return false;
    }

    // FALSE 3
    if (treeOne.val !== treeTwo.val ){
        return false;
    }

    // TRUE 2
    if (treeOne.val === treeTwo.val) {
        const sideOne = isSameTree(treeOne.right, treeTwo.left);
        const sideTwo = isSameTree(treeOne.left, treeTwo.right);

        return sideOne && sideTwo;

    }
    
}


// Very similar to same tree, but you need to pass in opposite sides
// (once you confirm existence) to the sameTree function
const isSymmetric = (root) => {
    const treeOne = root.left;
    const treeTwo = root.right;

    if (treeOne === null && treeTwo === null ){
        return true;
    }

    if (treeOne === null && treeTwo !== null) {
        return false;
    }

    if (treeOne !== null && treeTwo === null) {
        return false;
    }

    if (treeOne.val !== treeTwo.val ){
        return false;
    } else {

        const sideOne = isSameTree(treeOne.right, treeTwo.left);
        const sideTwo = isSameTree(treeOne.left, treeTwo.right);

        return sideOne && sideTwo;
    }
};
