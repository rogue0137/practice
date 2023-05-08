/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    // DON'T FORGET: you need the "new" keyword
    let curr = dummy = new ListNode(0, null);
  
    // move the next pointer to point to the next in the list
    while (list1 && list2) {
      if (list1.val < list2.val) {
          // if list1 is less than list2, set the curr.next to list1
          // you then need to move the pointer for list1 to it's next value
          curr.next = list1
          list1 = list1.next
      } else {
          // if list2 is less than or equal to list 1, set curr.next to list2
          // you then need to move the pointer for list2 to it's next value
          curr.next = list2
          list2 = list2.next
      }
      // for the while loop to not get stuck (and to actually advance)
      // you need to move the curr to it's next so you can set the value 
      // to something
      curr = curr.next
    }
  
    // your while loop checks that both list1 and list2 exist
    // when you have cycled through one entire list, you will merely
    // need to append the rest of it to curr
    curr.next = list1 || list2;
  
    // SOLVE 1: Use new List -- THIS
    // SOLVE 2: Use recursion
  
  
     return dummy.next;
  };
