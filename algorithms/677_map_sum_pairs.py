class MapSum(object):
    # Brute Force: insert O(n), sum O(1)
    def __init__(self):
        self.words = set()
        self.d = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        overwrite = key in self.words
        self.words.add(key)
        for i in range(1, len(key)+1):
            word = key[:i]
            if word in self.d and not overwrite:
                self.d[word] += val
            else:
                self.d[word] = val


    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.d.get(prefix, 0)



# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("apple", 3)
print obj.sum('apple')
print obj.sum('ap')
# obj.insert("app", 2)
# print obj.sum('ap')