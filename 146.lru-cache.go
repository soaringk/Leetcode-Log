package leetcode

// LRUCache lru cache
// 需要用到一个哈希表和一个双向链表，维护所有在缓存中的键值对。
// - 双向链表按照被使用的顺序存储键值对，靠近头部的键值对是最近使用的，而靠近尾部的键值对是最久未使用的。
// - 哈希表即为普通的哈希映射，缓存数据 -> 链表中的位置。
// 我们首先使用哈希表进行定位，找出缓存项在双向链表中的位置，随后将其移动到双向链表的头部，
//
// * 访问哈希表的时间复杂度为 O(1)，
// * 在双向链表的头部添加节点、在双向链表的尾部删除节点的复杂度也为 O(1)。
// * 而将一个节点移到双向链表的头部，可以分成「删除该节点」和「在双向链表的头部添加节点」两步操作，都可以在 O(1) 时间内完成。
//
// 在双向链表的实现中，使用一个伪头部（dummy head）和伪尾部（dummy tail）标记界限，
// 这样在添加节点和删除节点的时候就不需要检查相邻的节点是否存在。
type LRUCache struct {
	size       int
	capacity   int
	index      map[int]*DLinkedNode
	head, tail *DLinkedNode
}

type DLinkedNode struct {
	key, value int
	prev, next *DLinkedNode
}

// Constructor 初始化
func Constructor(capacity int) LRUCache {
	head := &DLinkedNode{} // dummy head
	tail := &DLinkedNode{} // dummy tail
	head.next = tail
	tail.prev = head
	return LRUCache{
		size:     0,
		capacity: capacity,
		index:    map[int]*DLinkedNode{},
		head:     head,
		tail:     tail,
	}
}

// Get 获取一个数据
// 判断key是否存在
// 1. 不存在，则返回 -1
// 2. 存在，则通过哈希表找到该节点在双向链表中的位置，并将其移动到链表的头部，最后返回该节点的值。
func (this *LRUCache) Get(key int) int {
	if node, ok := this.index[key]; ok {
		this.moveToHead(node)
		return node.value
	}
	return -1
}

// Put 加入一个数据
// 判断key是否存在
//  1. 不存在，
//     a. 使用 key 和 value 创建一个新的节点，在双向链表的头部添加该节点，并将 key 和该节点添加进哈希表中。
//     b. 然后判断双向链表的节点数是否超出容量，如果超出容量，则删除双向链表的尾部节点，
//     c. 并删除哈希表中对应的项；
//  2. 存在，则通过哈希表找到该节点在双向链表中的位置，并将其移动到链表的头部，最后返回该节点的值。
func (this *LRUCache) Put(key int, value int) {
	if node, ok := this.index[key]; ok {
		node.value = value
		this.moveToHead(node)
		return
	}
	node := &DLinkedNode{key: key, value: value}
	this.index[key] = node
	this.addToHead(node)
	this.size++
	if this.size > this.capacity {
		removed := this.removeTail()
		delete(this.index, removed.key)
		this.size--
	}
}

// 在双向链表中移动某个内容到队首，等价于先删再加
func (this *LRUCache) moveToHead(node *DLinkedNode) {
	this.removeNode(node)
	this.addToHead(node)
}

// 在双向链表中添加到队首
func (this *LRUCache) addToHead(node *DLinkedNode) {
	node.prev = this.head
	node.next = this.head.next
	this.head.next.prev = node
	this.head.next = node
}

// 删除内容，修改前后变量的指针，跳过自身即可
func (this *LRUCache) removeNode(node *DLinkedNode) {
	node.prev.next = node.next
	node.next.prev = node.prev
}

// 拿到队尾的元素，然后删除
func (this *LRUCache) removeTail() *DLinkedNode {
	tmp := this.tail.prev
	this.removeNode(tmp)
	return tmp
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
