def searchInsert(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    # If the array is empty, then target would be the first element
    if len(nums) == 0:
        return 0
    # The target is at position 0 or it should be placed at position 0
    if nums[0] >= target:
        return 0
    if nums[0] < 1 and len(nums) == 1:
        return 1
    for i in range(1, len(nums)):
        if nums[i] < target:
            continue
        if nums[i] == target:
            return i
        if nums[i] > target:
            return i
    return len(nums)
