
class Solution:
    def findMidSum(self, ar1, ar2, n): 
        if not ar1 or not ar2:
            return -1

        if n != len(ar2):
            return -1

        low = 0
        high = n

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = n - cut1
            l1 = float('-inf') if cut1 == 0 else ar1[cut1 - 1]
            r1 = float('inf') if cut1 == n else ar1[cut1]
            l2 = float('-inf') if cut2 == 0 else ar2[cut2 - 1]
            r2 = float('inf') if cut2 == n else ar2[cut2]

            if l1 <= r2 and l2 <= r1:
                return max(l1, l2) + min(r1, r2)
            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1

        return -1
            