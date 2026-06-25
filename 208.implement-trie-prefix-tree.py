#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Node:
    __slots__ = 'son', 'end'

    def __init__(self):
        self.son = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.son: # 不存在已有分支上就分裂
                cur.son[c] = Node()
            cur = cur.son[c] # 迭代到子树
        cur.end = True

    def find(self, word: str) -> int:
        cur = self.root
        '''前缀树可以想象成一条路径，每一个索引上的输入代表唯一一条道路的选择 "[1,1,3,2]"
        因此只要找到了，就可以往那条路径继续找（不可能在在其他路径上）；没找到就开辟新路径
        '''
        for c in word:
            if c not in cur.son: # 前缀树匹配失败
                return 0
            cur = cur.son[c]
        # （2=完全匹配，1=前缀匹配）
        return 2 if cur.end else 1

    def search(self, word: str) -> bool:
        return self.find(word) == 2


    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) != 0


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

obj = Trie()
obj.insert("apple")
obj.search("apple")
obj.search("app")
obj.startsWith("app")
obj.insert("app")
obj.search("app")
