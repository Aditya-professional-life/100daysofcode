def read(n: int, book: [int], target: int) -> str:
    # Write your code here.
    left = 0
    right = n -1
    book.sort()
    while left < right:
        sum = book[left] + book[right]
        if sum == target:
            return "YES"
        
        elif sum <target:
            left +=1
        else:
            right -=1
    return "NO"