class HashMap:
    def __init__(self, initial_capacity: int, load_factor: int):
        # basically an array of None's
        self.buckets = [ None for _ in range(initial_capacity)]
        self.size = 0
        # collision: different keys yield the same index
        self.collisions = 0
        # load_factor: how full we allow the  hashmap to get before we resize
        # and double the bucket size
        self.load_factor = load_factor

    def _generate_hash(self, key: str) -> int:
        hash_value = 0;
        string_key = list(str(key))

        for i in range(len(string_key)):
            char_code = ord(string_key[i])
            hash_value += char_code 
        return hash_value

    def get_load_factor(self):
        load_factor = self.size / len(self.buckets)
        return load_factor

    def _get_bucket_index(self, key):
        hash_value = self._generate_hash(key)
        bucket_index = hash_value % len(self.buckets)
        return bucket_index

    def _get_indexes(self, key):
        bucket_index = self._get_bucket_index(key)
        # entry index??
        # # may be able to do shortened ternary w/out if/else, using only or
        # values = if self.buckets[bucket_index]: self.buckets[bucket_index] else []
        # for i in range(len(values)):
        #     entry = values[i]
        #     if entry[key] == key:
        #         return bucket_index, i 
        return bucket_index

    # def _rehash(self, new_capicity: int):
    #     new_map = HashMap(new_capicity)
    #     for key in self.keys:
    #         # add key and values to new map?
    #     self.buckets = new_map.buckets
    #     self.collisions = new_map.collisions
    #     self.keys = new_map.keys 

    def insert(self, key, value):
        bucket_index = self._get_indexes(key)
        print(f'bucket index: {bucket_index}')
        if self.buckets[bucket_index] is None:
            self.buckets[bucket_index] = []
        self.buckets[bucket_index].append(( key, value )) 
        self.size += 1
        #     if len(self.buckets[bucket_index]) > 1:
        #         self.collisions += 1
        # else:
        #     self.buckets[bucket_index][entry_index] = [(key, value)]
        # # rehash check
        # if self.load_factor > 0 and self.get_load_factor() > this.load_factor:
        #     self._rehash(len(self.buckets) * 2)

    def delete(self, key):
        bucket_index = self._get_indexes(key)
        # this should remove element
        del self.buckets[bucket_index][0]
        self.size -= 1

    # def has(self, key):
    #     if key in self.keys:
    #         return True
    #     return False

    def get_value(self, key):
        bucket_index = self._get_indexes(key)
        value = self.buckets[bucket_index][0][1]
        return value

hashmap = HashMap(2, 0)
print(f'hashmap: {hashmap.buckets}\nsize: {hashmap.size}')
hashmap.insert('songs', 2)
hashmap.insert('rat', 7)
hashmap.insert('dog', 1)
hashmap.insert('art', 8)
print(f'hashmap: {hashmap.buckets}\nsize: {hashmap.size}')
hashmap.delete('songs')
print(f'hashmap: {hashmap.buckets}\nsize: {hashmap.size}')
rat_value = hashmap.get_value('rat')
print(f'rat value: {rat_value}')

# print(hashmap.buckets)
# print(f'collisions: {hashmap.collisions}')
# 
# Notes to self
# - raise errors

# IMPORTANT Notes (from online)
# - Not every bucket has anything in - we're reserving more space than we strictly need (space vs. speed is a classic computing trade-off).
# - Using a hash to determine the bucket means we can quickly (hopefully O(1)) find out where we should be looking, rather than searching through the whole table. This is why: hash speed is important - if it takes ages to calculate the hash, we lose the advantage; and hash stability is important - if you get a different hash for the same key, you can't find it again;
# - Some buckets have more than one thing in, in which case we fall back to a linear search O(len(bucket)). This is why hash distribution is important - if everything ended up in the same bucket (e.g. def _hash(self): self.hash = 42, this is known as hash collision) we're back to a O(n) search through everything.