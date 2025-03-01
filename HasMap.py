# class HashMap:
#     def __init__(self, size=100) -> None:
#         self.size = size
#         self.buckets = [[] for _ in range(size)]

#     def _hash(self, key):
#         return hash(key) % self.size

#     def put(self, key, value):
#         index = self._hash(key)
#         bucket = self.buckets[index]

#         for i, (k, v) in enumerate(bucket):
#             if k == key:
#                 bucket[i] = (key, value)
#                 return

#         bucket.append((key, value))

#     def get(self, key):
#         index = self._hash(key)
#         bucket = self.buckets[index]

#         for k, v in bucket:
#             if k == key:
#                 return v

#         return None

#     def remove(self, key):
#         index = self._hash(key)
#         bucket = self.buckets[index]

#         for i, (k, v) in enumerate(bucket):
#             if k == key:
#                 del bucket[i]
#                 return

#     def __str__(self):
#         return str([{k: v for k, v in bucket} for bucket in self.buckets if bucket])

# hash_map = HashMap()

# hash_map.put("augusto", 30)
# hash_map.put("matheus", 25)
# hash_map.put(17, ("cachorro", 13))

# print(hash_map)
# print(hash_map.get("augusto"))
# print(hash_map.remove("augusto"))
# print(hash_map.get("augusto"))


# MY IMPLEMENTATION
class HashMap:
    def __init__(self, size=100) -> None:
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v)in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return print("Chave atualizada com sucesso")

        bucket.append((key, value))
        return print("Nova chave adicionada com sucesso")

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for k, v in bucket:
            if k == key:
                return print(v)

        return print("Bucket não encontrado")

    def remove(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]

        return print("Chave deletada com sucesso!")

hash_map= HashMap()
hash_map.put("Nome", "gabriel")
hash_map.put("Idade", 21)
hash_map.get("Nome")
hash_map.remove("Idade")
hash_map.get("Idade")