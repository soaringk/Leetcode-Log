package leetcode

// isValid TODO
// 20. 有效的括号
// stack
func isValid(s string) bool {
	if len(s)%2 != 0 {
		return false
	}
	stack := make([]byte, 0, len(s)/2)
	for i := 0; i < len(s); i++ {
		b := s[i]
		switch b {
		case '[', '{', '(':
			stack = append(stack, b)
		case ']':
			if len(stack) == 0 || stack[len(stack)-1] != '[' {
				return false
			}
			stack = stack[:len(stack)-1]
		case '}':
			if len(stack) == 0 || stack[len(stack)-1] != '{' {
				return false
			}
			stack = stack[:len(stack)-1]
		case ')':
			if len(stack) == 0 || stack[len(stack)-1] != '(' {
				return false
			}
			stack = stack[:len(stack)-1]
		default:
		}
	}
	return len(stack) == 0
}
