# Find median of two sorted arrays
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    i = 0
    j = 0
    new_array = []
    while (i < len(nums1) and j < len(nums2)):
        if (nums1[i] < nums2[j]):
            new_array.append(nums1[i])
            i += 1
        else:
            new_array.append(nums2[j])
            j += 1
    if (i == len(nums1)):
        new_array += nums2[j:]
    else:
        new_array += nums1[i:]
    if (len(new_array) % 2 == 1):
        index = int(len(new_array) / 2)
        return new_array[index]
    else:
        index1 = int(len(new_array) / 2 - 1)
        index2 = int(len(new_array) / 2)
        return (new_array[index1] + new_array[index2]) / 2
