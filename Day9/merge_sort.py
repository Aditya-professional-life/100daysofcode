class Solution:
    def merge(self, arr, l, m, r):
        i = 0
        j = 0
        k = l  # Start from the left index
    
        left = arr[l:m + 1]  # Note the slice indices
        right = arr[m + 1:r + 1]
    
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
    
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
    
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        # code here
    def mergeSort(self,arr, l, r):
        m = mid = l+(r-l)//2
        if l <r:
            self.mergeSort(arr,l,m)
            self.mergeSort(arr,m+1,r)
            self.merge(arr,l,m,r)