class LRUCache {
    private maxSize: number;
    private map: Map<number, number>;
    private order: number[];
    
    constructor(capacity: number) {
        this.maxSize = capacity;
        this.map = new Map();
        this.order = [];
    }

    get(key: number): number | undefined {
        // if exists, return value
        if (this.map.has(key)) {
            // find value in queue and remove it
            const indexOfKey = this.order.indexOf(key);
            this.order.splice(indexOfKey, 1);
            // add value to end of queue
            this.order.push(key);
            const value = this.map.get(key);
            return value;
        } else {
            return -1;
        }


    }

    put(key: number, value: number): void {
        // maxSize = 2
        // [ 2 , 1]
        // map = { 2: 6, 1: 5}
      

        // if already exists, update value
        if (this.map.has(key)) {
            this.map.set(key, value);
            // find value in queue and remove it
            const indexOfKey = this.order.indexOf(key);
            this.order.splice(indexOfKey, 1);
            // add value to end of queue
            this.order.push(key);
        } else {
            if (this.order.length === this.maxSize) {
                this.map.delete(this.order[0]);
                this.order.shift();
            }
            this.map.set(key, value);
            // add value to end of queue
            this.order.push(key);
        }
    }

}

/**
 * Your LRUCache object will be instantiated and called as such:
 * var obj = new LRUCache(capacity)
 * obj.put(key,value)
 * var param_1 = obj.get(key)
 */
