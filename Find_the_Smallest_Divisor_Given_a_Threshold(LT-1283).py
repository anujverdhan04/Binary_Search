class Solution:
    def sumByD(self ,nums :List[int] , Diviser: int) -> int:
        n = len(nums)
        total_sum = 0
        for i in range(n):
           total_sum += math.ceil(nums[i] / Diviser)
        return total_sum 
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        low = 1
        high = max(nums)

        while low<= high:
            mid = (low+high)//2
            if self.sumByD(nums, mid) <= threshold:
                high = mid -1
            else:
                low = mid+1
        return low            
        
        