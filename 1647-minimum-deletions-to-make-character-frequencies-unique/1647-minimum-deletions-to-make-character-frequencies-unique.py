from collections import Counter as counter

class Solution:
    def minDeletions(self, s: str) -> int:
        counts = sorted(counter(s).values())
        occoured = set()

        operations_needed = 0
        for item in counts:
            if item not in occoured:
                occoured.add(item)
            else:
                tmp = item
                while tmp in occoured:
                    tmp -= 1
                    operations_needed += 1
                if tmp != 0:
                    occoured.add(tmp)

        return operations_needed