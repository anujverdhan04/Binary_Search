class Solution:
    def countpartitions(self, nums: List[int], maxSum: int) -> int:
        n = len(nums)
        partition = 1
        subarraySum = 0
        for i in range(n):
            if subarraySum + nums[i] <= maxSum:
                subarraySum += nums[i]
            else:
                partition += 1
                subarraySum = nums[i]
        return partition

    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        while low < high:
            mid = (low + high) // 2
            if self.countpartitions(nums, mid) <= k:
                high = mid
            else:
                low = mid + 1

        return low
