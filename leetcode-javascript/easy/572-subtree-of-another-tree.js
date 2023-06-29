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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
const isSameTree = function (treeOne, treeTwo) {

    // base cases: do treeOne and treeTwo exist
    // if both trees do NOT exist they are the same
    if (treeOne === null && treeTwo === null ) {
        return true;
    }
    // if treeOne exists, but treeTwo does not exist, they are not the same
    if (treeOne !== null && treeTwo === null ) {
        return false;
    }
    // if treeOne does not exist, but treeTwo exists, they are not the same
    if (treeOne === null && treeTwo !== null) {
        return false;
    }

    // recursive cases
    // if both trees exist, check their values
    if (treeOne.val === treeTwo.val ) {
        const leftSide = isSameTree(treeOne.left, treeTwo.left);
        const rightSide = isSameTree(treeOne.right, treeTwo.right);
        return leftSide && rightSide;
    } else {
        return false;
    }

}
const isSubtree = function(root, subRoot) {
    // base case 1
    if (!root) return false;

    const isRootSame = isSameTree(root, subRoot);
    // base case 2
    if (isRootSame) {
        return true;
    } else {
    // recursive case
        const leftRoot = isSubtree(root.left, subRoot);
        const rightRoot = isSubtree(root.right, subRoot);

        const isEitherSideSame = leftRoot || rightRoot;
        return isEitherSideSame;
    }

    
};
