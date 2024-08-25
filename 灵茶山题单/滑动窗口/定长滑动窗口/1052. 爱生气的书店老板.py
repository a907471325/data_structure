class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:


        total = 0
        max_angry = 0
        cur_angry = 0

        for i, x in enumerate(customers):
            if grumpy[i] == 0:
                total += x
            else:
                cur_angry += x

            if i < minutes - 1:
                continue

            max_angry = max(max_angry, cur_angry)
            if grumpy[i- minutes + 1] == 1:
                cur_angry -= customers[i- minutes + 1]
        return total + max_angry

