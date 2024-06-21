class Solution:
    def binarysearch(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low = 0
        high = n-1
        
        while low <= high:
            mid = (low+high)//2
            if(nums[mid] == target):
                return True
            elif(nums[mid] < target):
                low = mid+1
            else:
                high = mid-1 
        return False         

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        
        for i in range(rows):
            if matrix[i][0] <= target and target <= matrix[i][columns-1]:
                if self.binarysearch(matrix[i] , target):
                    return True
        return False

'''
        if not matrix or not matrix[0]:
            return False
        
        rows = len(matrix)
        columns = len(matrix[0])
        
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == target:
                    return True
        return False
'''        