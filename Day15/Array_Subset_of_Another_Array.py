def isSubset( arr1, arr2, n, m):
    frequency = {}

    # Count the frequency of each element in arr1
    for i in range(n):
        if arr1[i] in frequency:
            frequency[arr1[i]] += 1
        else:
            frequency[arr1[i]] = 1

    # Check if arr2 elements are present in arr1
    for i in range(m):
        if arr2[i] in frequency and frequency[arr2[i]] > 0:
            frequency[arr2[i]] -= 1
        else:
            return "No"

    return "Yes"
    