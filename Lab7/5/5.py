from MaxHeap import MaxHeap


heap = MaxHeap()
alist = [10, 91, 25, 23, 45, 50, 30, 35, 63, 65, 81]

heap.buildHeap(alist)
print(list(reversed(sorted(alist))))
print("size:", heap.currentSize)
print(heap.delMax())
print(heap.delMax())
print(heap.delMax())
print(heap.delMax())
print(heap.delMax())
print(heap.delMax())
