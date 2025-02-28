# EASY
# https://leetcode.com/problems/design-hashset/
# MY SOLUTION PROBLEM

class HashSet:
    def __init__(self) -> None:
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def add(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        if key not in bucket:
            bucket.append(key)

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        if key in bucket:
            bucket.remove(key)

    def constains(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        
        if key in bucket:
            return True
        
        return False
    
hash_map = HashSet()
print(hash_map.add("Gabriel"))
print(hash_map.add("Matheus"))
print(hash_map.remove("Matheus"))
print(hash_map.constains("Gabriel"))
print(hash_map.constains("Matheus"))
print(hash_map.remove("Matheus"))