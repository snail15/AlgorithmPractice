def search(self, nums: List[int], target: int) -> int:
    
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start ) // 2

        if target == nums[mid]:
            return mid
        
        if nums[mid] >= nums[start]:
            if target < nums[start] or target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if target > nums[end] or target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
    
    return -1