const assert = require('assert');

/*
Design an cache with a configurable maximum size and the following properties:

- “Entries” are composed of a key-value pair.
- Inserting an entry with a key that already exists in the cache, simply replaces the existing entry.
- Fetching an entry by key returns the value of the entry if it exists in the cache. Otherwise, an error should be returned.
- An “entry” is considered “accessed” if it is fetched from or inserted into the cache.
- When the cache is full, inserting a new entry results in the oldest entry accessed being evicted from the cache.
- Ideally, the cache should be generic, but it must at least accept strings for both keys and values.

The cache should implement an interface similar to:

```jsx
interface Cache<K, V> {
    public V get(K key);
    public V put(K key, V value);
}

// Examples
c = Cache(3)
c.put("a", "1") // evicted
c.put("b", "2")
c.put("c", "3")
c.put("d", "4")

c.put("a", "1")
c.put("b", "2") // evicted
c.put("c", "3")
c.get("a")
c.put("d", "4")

c.put("a", "1")
c.put("b", "2") // evicted
c.put("c", "3")
c.put("a", "5")
c.put("d", "4")
```
*/
class Node {
  constructor(key, value){
    this.key = key;
    this.value = value;
    this.next = null;
    this.prev = null;
  }
}
class Cache {
  constructor(maxSize) {
    this.maxSize = maxSize;
    this.currSize = 0;
    this.map = new Map();
    this.head = null;
    this.tail = null;
  }

  get(key) {
    const node = this.map[key];

    if (node === undefined){
      return 'Error';
    }
    
    // put node at the end
    this.moveNodeToEnd(node);
    
    const value = this.map[key].value;

    return value ;
  }


  put(key, value) {

    if (this.map[key]) {
      this.map[key].value = value;
      // move node to end
      this.moveNodeToEnd(this.map[key]);
    } else {
      // add node 
      this.addNode(key, value);
    }
  }

  addNode(key, value) {
    const node = new Node(key, value);

    // Check for head, if it doesn't exist
    // Make this node the head
    const prevHead = this.head;
    if (prevHead === null) {
      this.head = node;
    } 
    if (this.currSize === this.maxSize) {
      const currHead = this.head
      const newHead = currHead.next;
      this.head = newHead;
      this.head.prev = null;
      delete this.map[currHead.key];
      this.currSize--;
    }
    const prevTail = this.tail;
    // Check for tail, if it doesn't exist
    // Make this node the tail
    // else update the tail to be this node
    // Move it to the end
    if (prevTail){
      prevTail.next = node;
      this.tail = node;
      this.tail.prev = prevTail;
    } else {
      this.tail = node;
    }
    this.map[key] = node;
    this.currSize++;
  }
    
  moveNodeToEnd(node) {
    // if node is head, make next node the head
    if (this.head === node){
      this.head = node.next;
      this.head.prev = null;
    } else {
      const prevNode = node.prev; 
      prevNode.next = node.next;
    }
    
    if (this.tail !== node){
      const prevTail = this.tail;
      prevTail.next = node;
      node.prev = prevTail;   
    }
    
    node.next = null;
    this.tail = node;
    }

}

// where 3 is maxSize
const c = new Cache(3);
c.put("a", "1"); // evicted
c.put("b", "2");
c.put("c", "3");
c.put("d", "4");
assert.equal(c.get("a"), "Error");

c.put("a", "1");
c.put("b", "2"); // evicted
c.put("c", "3");
assert.equal(c.get("a"), "1");
c.put("d", "4");
assert.equal(c.get("b"), "Error");

c.put("a", "1");
c.put("b", "2"); // evicted
c.put("c", "3");
c.put("a", "5");
c.put("d", "4");
assert.equal(c.get("b"), "Error");
assert.equal(c.get("a"),5); // Added assertion to test that value for Node A wa actually updated

// console.log('HEAD: ', c.head);
// console.log('TAIL: ', c.tail);
// console.log('MAP: ', c.map);
