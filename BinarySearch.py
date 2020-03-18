def bin_search(arr, left, high, key):
    
        if key in arr:
            return(arr.index(key))
        else:
            return(-1)



Input:
2
5
1 2 3 4 5 
4
5
11 22 33 44 55
445

Output:
3
-1