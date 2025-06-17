package main

import (
	"sync"
)

// 使用互斥锁实现读写锁
type RWMutex struct {
	mu        sync.Mutex
	readers   int
	writeWait bool
}

func (rw *RWMutex) RLock() {
	rw.mu.Lock()
	defer rw.mu.Unlock()
	for rw.writeWait {
		rw.mu.Unlock()
		rw.mu.Lock()
	}
	rw.readers++
}
func (rw *RWMutex) RUnlock() {
	rw.mu.Lock()
	defer rw.mu.Unlock()
	rw.readers--
	if rw.readers == 0 {
		rw.writeWait = false
	}
}
func (rw *RWMutex) Lock() {
	rw.mu.Lock()
	defer rw.mu.Unlock()
	for rw.readers > 0 || rw.writeWait {
		rw.mu.Unlock()
		rw.mu.Lock()
	}
	rw.writeWait = true
}
func (rw *RWMutex) Unlock() {
	rw.mu.Lock()
	defer rw.mu.Unlock()
	rw.writeWait = false
}

func main() {
	rw := &RWMutex{}
	rw.RLock()
	rw.RUnlock()
	rw.Lock()
	rw.Unlock()
}
