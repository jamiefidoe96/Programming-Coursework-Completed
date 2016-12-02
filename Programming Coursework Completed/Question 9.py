def binary (array, low, high):
    while array:
        mid = len(array) // 2        
        if array[mid] in range(low, high+1):   0(n^n)        
            return True
        elif array[mid] < high:                0(n)
            array = array[mid+1:]
        elif array[mid] > low:                 O(n)    
            array = array[0:mid] # The run time bounds of this binary search is O(log(n^n))
        
    return False
