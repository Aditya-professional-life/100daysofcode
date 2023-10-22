    def minimumPlatform(self,n,arr,dep):
        arr.sort()
        dep.sort()
    
        i = 0
        j = 0
        result = 0
        plat = 0
    
        while i < n and j < n:
            if arr[i] <= dep[j]:
                plat += 1
                i += 1
            else:
                plat -= 1
                j += 1
    
            result = max(result, plat)
    
        return result
            