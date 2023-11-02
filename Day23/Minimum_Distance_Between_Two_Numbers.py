class Solution:
    def minDist(self, arr, n, x, y):
        if x not in arr or y not in arr:
            return -1
        index_of_x = -1
        index_of_y = -1
        min_distance = float('inf')

        for i in range(n):
            if arr[i] == x:
                index_of_x = i
                if index_of_y != -1:
                    min_distance = min(min_distance, abs(index_of_x - index_of_y))

            if arr[i] == y:
                index_of_y = i
                if index_of_x != -1:
                    min_distance = min(min_distance, abs(index_of_x - index_of_y))

        return min_distance