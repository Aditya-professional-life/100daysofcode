class Solution:
    def subArraySum(self, arr, n, s):
        start = 0
        curr_sum = arr[0]

        for i in range(1, n):  # Changed the starting index to 1
            curr_sum += arr[i]
            while curr_sum > s and start < i:
                curr_sum -= arr[start]
                start += 1

            if curr_sum == s:
                return arr[start],arr[i+]  # Include arr[i] in the subarray

        return -1 