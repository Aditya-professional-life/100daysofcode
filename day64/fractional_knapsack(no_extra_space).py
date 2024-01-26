

class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, profit, weight, capacity):
        for i in range(len(profit)):
            profit[i] /= weight[i]

        profit.sort(reverse = True)
        max_value = 0

        for i in range(len(profit)):
            if capacity >= weight[i]:
                max_value = max_value + profit[i] *weight[i]
                capacity = capacity - weight[i]

            else:
                max_value = max_value +profit[i]* capacity
                break


        return max_value        
    

sol = Solution()
profit = [60, 100, 120]
weight = [10, 20, 30]
capacity = 50
print("Maximum value in knapsack:", sol.fractionalknapsack(profit, weight, capacity))