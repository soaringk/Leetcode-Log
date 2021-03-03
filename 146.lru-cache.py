#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, key, val, **kwargs):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class linked_list:
    def __init__(self):
        head = Node(0, 0)
        tail = Node(0, 0)
        head.next = tail
        tail.prev = head
        self.head = head
        self.tail = tail
        self.__size = 0

    def addLast(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.__size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.__size -= 1

    def removeFirst(self):
        if self.head.next == self.tail:
            return None
        first = self.head.next
        self.remove(first)
        return first

    def size(self):
        return self.__size


class LRUCache:
    def __init__(self, capacity: int):
        self.hash_map = {}
        self.cache = linked_list()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if not key in self.hash_map:
            return -1
        self.makeRecent(key)
        return self.hash_map.get(key).val

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.deleteKey(key)
            self.addRecent(key, value)
            return
        if self.capacity == self.cache.size():
            self.removeLeastRecent()

        self.addRecent(key, value)

    # 将某个 key 提升为最近使用的
    def makeRecent(self, key):
        node = self.hash_map.get(key)
        self.cache.remove(node)
        self.cache.addLast(node)

    # 添加最近使用的元素
    def addRecent(self, key, val):
        node = Node(key, val)
        self.cache.addLast(node)
        self.hash_map[key] = node

    # 删除某一个 key
    def deleteKey(self, key):
        node = self.hash_map.get(key)
        self.cache.remove(node)
        self.hash_map.pop(key)

    # 删除最久未使用的元素
    def removeLeastRecent(self):
        node = self.cache.removeFirst()
        deleted_key = node.key
        self.hash_map.pop(deleted_key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

s = LRUCache(2)
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
s.put(1, 1)
s.put(2, 2)
s.get(1)
s.put(3, 3)
s.put(4, 4)
