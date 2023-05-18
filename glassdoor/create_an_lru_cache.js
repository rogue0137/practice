const _ = require('lodash');
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
  constructor(key, value) {
    this.key = key;
    this.value = value;
    this.next = null;
    this.prev = null;
  }

}

class Cache {
  
  constructor(maxSize) {
    this.map = new Map();
    this.maxSize = maxSize;
    this.head = null; // head will be last recently accessed
    this.tail = null; // tail will be most recently accessed
  }
  
  
  put = (key, value) => {

    if (this.map.has(key)){
      // update value
      this.map.get(key).value = value;
      // If the key already existed it should be removed and then readded to show it was recently accessed
      this.deleteNode(key);
      this.addNode(key, value);
    } else {
      if (this.map.size >= this.maxSize) {
        // remove the head
        const leastRecentlyAccessedKey = this.head.key;
        this.deleteNode(leastRecentlyAccessedKey);
        this.map.delete(leastRecentlyAccessedKey);
      }
      // Add new node and then add to the map
      this.addNode(key, value);
      this.map.set(key, this.tail); 
    }
    
  }
  
  get = (key) => {
    // Check for key existence
    if (!this.map.has(key)) {
      return "Error";
    } 

    const value = this.map.get(key).value;
    // Since this key/value pair was accessed it should be
    // moved to last to show it was recently accessed.
    this.deleteNode(key);
    this.addNode(key, value);

    return value;
    
  }

  // Recently accessed nodes will be moved by
  // deleting them and then re-adding them.
  addNode = (key, value) => {
    const node = new Node(key, value);

    if (this.tail === null) {
      // no nodes yet, so make it the head
      this.head = node;
    } else {
      this.tail.next = node;
      node.prev = this.tail;
    }

    // regardless of the above, ensure it becomes the tail
    this.tail = node;
  }

  // Delete?
  deleteNode = (key) => {
    const node = this.map.get(key);

    // Prev pointer
    if (node.prev === null || node.prev === undefined) {
      // if there are no previous nodes, set this node's next to the head
      this.head = node?.next;
    } else {
      node.prev.next = node.next
    }

    // Next pointer
    if (node.next === null || node.prev === undefined) {
      // if there are no later nodes, set this node's prev as the tail
      this.tail = node?.prev
    } else {
      node.next.prev = node.prev
    }
  
  }
  
}

// where 3 is maxSize
const c = new Cache(3)
c.put("a", "1") // evicted
c.put("b", "2")
c.put("c", "3")
c.put("d", "4")
assert.equal(c.get("a"), "Error");

c.put("a", "1")
c.put("b", "2") // evicted
c.put("c", "3")
assert.equal(c.get("a"), "1");
c.put("d", "4")
assert.equal(c.get("b"), "Error");

c.put("a", "1")
// c.put("b", "2") // evicted
// c.put("c", "3")
// c.put("a", "5")
// c.put("d", "4")
// assert.equal(c.get("b"), "Error");

/* 
Hi, Jameel,

Thank you for the opportunity to continue working on this problem.
I got everything up to line 157 to pass. However, when I got to 158, I kept getting:

solution.js:123
    if (node.prev === null || node.prev === undefined) {
             ^

TypeError: Cannot read properties of undefined (reading 'prev')

I trouble shooted for a bit, but have to go pick up the kids now. 

Have a lovely vacation!
~Krys
*/
