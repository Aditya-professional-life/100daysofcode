#User function Template for python3
class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
            p = self.partition(arr, low, high)
            self.quickSort(arr, low, p)
            self.quickSort(arr, p + 1, high)

    def partition(self, arr, low, high):
        pivot = arr[low]
        i = low + 1
        j = high
        while True:
            while i <= j and arr[i] < pivot:
                i += 1
            while i <= j and arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            else:
                break
        arr[low], arr[j] = arr[j], arr[low]
        return j


