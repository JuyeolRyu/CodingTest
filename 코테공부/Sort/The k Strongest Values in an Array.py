############################################################################
#1471. The k Strongest Values in an Array                                  #
#https://leetcode.com/problems/the-k-strongest-values-in-an-array/         #
############################################################################

class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr = sorted(arr)
        median = arr[(len(arr)-1)//2]
        lst = []
        
        for num in arr:
            lst.append([num,abs(num-median)])
            
        lst = sorted(lst, key = lambda x: (x[1],x[0]),reverse = True)
        return [lst[idx][0] for idx in range(k)]