from BoundedMinHeap import MinHeap


heap = MinHeap(6)
alist = [10, 91, 25, 23, 45, 50, 30, 35, 63, 65, 81]

heap.buildHeap(alist)

print("maxSize:", heap.maxElements)
print("size:", heap.currentSize)
print(heap.delMin())
print(heap.delMin())
print(heap.delMin())
print(heap.delMin())
print(heap.delMin())
print(heap.delMin())
