class Solution:
    def majorityElement(self, A, n):
        candidate = None
        count = 0

        # Find a potential candidate for the majority element
        for element in A:
            if count == 0:
                candidate = element
            if element == candidate:
                count += 1
            else:
                count -= 1

        # Verify if the candidate is the majority element
        count = 0
        for element in A:
            if element == candidate:
                count += 1

        if count > n / 2:
            return candidate
        else:
            return -1
