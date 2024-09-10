
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        n = len(arr)
        target = n - k

        i=0
        j=n-1
        while i < j and target != 0:
            left = arr[i]
            right = arr[j]
            if abs(left-x) > abs(right-x):
                i += 1
            else:
                j -= 1
            target -= 1

        return arr[i:j+1]
