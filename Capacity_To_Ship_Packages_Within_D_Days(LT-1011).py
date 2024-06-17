class Solution:
    def findDays(self , weights: List[int], capacity:int) -> int:
        n= len(weights)
        days =1
        load = 0
        for i in range(n):
            if load + weights[i] > capacity:
                days +=1
                load = weights[i]
            else:
                load+=weights[i]
        return days            
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)
        low = max(weights)
        high= sum(weights)
        while low<=high:
            mid=(low+high)//2
            if self.findDays(weights , mid) <=days:
                high = mid-1
            else:
                low = mid+1
        return low            
        