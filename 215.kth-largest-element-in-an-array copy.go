package leetcode

type heap []int

// buildHeap 只要按照顺序，把切片下标为n/2到1的节点依次堆化，最后就会把整个切片堆化
func buildHeap(nums []int) heap {
	lastParent := len(nums)/2 - 1      // 初始建堆，从最后一个父节点开始调整
	for i := lastParent; i >= 0; i-- { // O(n)
		heapify(nums, len(nums), i) // O(logN)
	}
	return nums
}

// heapify 对下标为i的节点进行堆化， n表示堆的最后一个节点下标
// 2i,2i+1
func heapify(nums []int, n, i int) {
	if i >= n {
		return
	}
	// n 表示需要调整的节点总数
	// i 表示要开始调整的节点下标
	leftI := 2*i + 1
	rightI := 2*i + 2
	parentI := i
	if leftI < n && nums[leftI] > nums[parentI] {
		parentI = leftI
	}
	if rightI < n && nums[rightI] > nums[parentI] {
		parentI = rightI
	}

	if i != parentI {
		nums[i], nums[parentI] = nums[parentI], nums[i]
		heapify(nums, n, parentI) // 如果发生了交换，则递归地对被交换下来的数字进行调整.最多次数为树的高度，O(logN)级别
	}
}

// findKthLargest TODO
// 215. 数组中的第 k 个最大元素
func findKthLargest(nums []int, k int) int {
	h := buildHeap(nums)
	for i := 0; i < k-1; i++ {
		h[0], h[len(h)-1-i] = h[len(h)-1-i], h[0]
		heapify(h, len(h)-1-i, 0)
	}
	return h[0]
}
