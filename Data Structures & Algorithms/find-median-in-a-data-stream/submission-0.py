class MedianFinder:

    def __init__(self):
        # two heaps, large, small, minheap, maxheap
        # heaps should be equal size
        self.small, self.large = [],[]

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        if len(self.small) > len(self.large) + 1:
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1*val)
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1*self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-1*self.small[0]+self.large[0])/2.0
        

# class MaxHeap:
#     def __init__(self):
#         self.heap = []

#     def parent(self, index):
#         return (index - 1) // 2

#     def left_child(self, index):
#         return 2 * index + 1

#     def right_child(self, index):
#         return 2 * index + 2

# -----------------------------------------------------------

# def insert(self, key):
#     self.heap.append(key)
#     self.heapify_up(len(self.heap) - 1)

# def heapify_up(self, index):
#     while index != 0 and self.heap[self.parent(index)] < self.heap[index]:

#         self.heap[self.parent(index)], self.heap[index] = \
#         self.heap[index], self.heap[self.parent(index)]

#         index = self.parent(index)

# ------------------------------------------------------------------------

# def extract_max(self):
#     if not self.heap:
#         return None

#     maximum = self.heap[0]
#     self.heap[0] = self.heap[-1]
#     self.heap.pop()
#     self.heapify_down(0)
#     return maximum

# def heapify_down(self, index):
#     size = len(self.heap)
#     largest = index
#     while True:
        # left = self.left_child(index)
        # right = self.right_child(index)

        # if left < size and self.heap[left] > self.heap[largest]:
        #     largest = left
        # if right < size and self.heap[right] > self.heap[largest]:
        #     largest = right
        # if largest != index:
        #     self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
        # index = largest
        # else:
            #   break
# --------------------------------------------------------------------------

# def build_heap(self, array):
#     self.heap = array[:]
#     for i in range(len(self.heap) // 2 - 1, -1, -1):
#         self.heapify_down(i)

# -----------------------------------------------------------------------

