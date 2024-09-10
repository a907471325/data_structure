class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        n = len(plants)
        remainA = capacityA
        remainB = capacityB
        res = 0
        for i in range(n):
            j = n - 1 - i

            if i > j:
                break
            if i == j:
                if remainA < remainB:
                    if remainB >= plants[i]:
                        remainB -= plants[i]
                    else:
                        res += 1
                        remainB = capacityB - plants[i]
                else:
                    if remainA >= plants[i]:
                        remainA -= plants[i]
                    else:
                        res += 1
                        remainA = capacityA - plants[i]
            else:
                if remainB >= plants[j]:
                    remainB -= plants[j]
                else:
                    res += 1
                    remainB = capacityB - plants[j]

                if remainA >= plants[i]:
                    remainA -= plants[i]
                else:
                    res += 1
                    remainA = capacityA - plants[i]
        return res


