class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.queue = nums
        self.k = k

    def add(self, val: int) -> int:
        self.queue.append(val)
        self.queue.sort()
        tmp = []
        for i in range(0, self.k):
            tmp.append(self.queue[-i - 1])
        return tmp[-1]
        
