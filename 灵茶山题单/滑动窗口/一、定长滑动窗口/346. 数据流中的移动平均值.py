class MovingAverage:
    size = 0
    nums = None
    wsum = 0

    def __init__(self, size: int):
        self.size = size
        self.nums = []

    def next(self, val: int) -> float:
        self.wsum += val
        self.nums.append(val)
        if len(self.nums) < self.size:
            return self.wsum / len(self.nums)

        if len(self.nums) == self.size:
            res = self.wsum / len(self.nums)
            self.wsum -= self.nums[0]
            self.nums = self.nums[1:]
            return res

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)