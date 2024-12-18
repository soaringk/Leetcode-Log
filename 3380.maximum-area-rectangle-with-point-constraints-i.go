package leetcode

func maxRectangleArea(points [][]int) int {
	var result int64 = -1
	for i := range points {
	OUTER:
		for j := range points {
			p1, p2 := points[i], points[j]
			x1, y1, x2, y2 := p1[0], p1[1], p2[0], p2[1]
			if (x1 == x2) || (y1 == y2) {
				continue
			}
			// swap to make square index 2 is greater than 1
			// this should not affect the production
			if x1 > x2 {
				x1, x2 = x2, x1
			}
			if y1 > y2 {
				y1, y2 = y2, y1
			}
			for k := range points {
				pk := points[k]
				xk, yk := pk[0], pk[1]
				if (xk >= x1 && xk <= x2) || (yk >= y1 && yk <= y2) {
					continue OUTER
				}
			}
			product := abs(int64(x2-x1)) * abs(int64(y2-y1))
			if product > result {
				result = product
			}
		}
	}
	return int(result)
}

func abs(n int64) int64 {
	y := n >> 63
	return (n ^ y) - y
}
