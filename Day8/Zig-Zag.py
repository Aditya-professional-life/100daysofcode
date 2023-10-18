

class Solution:
    # Program for zig-zag conversion of array
    def zigZag(self, arr, n):
        for i in range(n-1):
            if i%2 == 0:
                if arr[i] > arr[i+1]:
                    arr[i] , arr[i+1] = arr[i+1],arr[i]
            elif i%2 != 0:
                if arr[i] < arr[i+1]:
                    arr[i] , arr[i+1] = arr[i+1],arr[i]
                
        return arr