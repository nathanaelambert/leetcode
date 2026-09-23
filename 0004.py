def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    if (len(nums1) > len(nums2)):
        nums1, nums2 = nums2, nums1
    half = (len(nums1) + len(nums2)+1) // 2
    
    left, right = 0, len(nums1)
    while left <= right:
        partition1 = left + (right - left) // 2
        partition2 = half - partition1
        left1 = nums1[partition1 - 1] if partition1 - 1 >= 0 else float("-inf")
        right1 = nums1[partition1] if partition1 < len(nums1) else float("inf")
        left2 = nums2[partition2 - 1] if partition2 - 1 >= 0 else float("-inf")
        right2 = nums2[partition2] if partition2 < len(nums2) else float("inf")
        
        if left1 <= right2 and left2 <= right1:
            smaller_med = max(left1, left2)
            bigger_med = min(right1, right2) if (len(nums1) + len(nums2)) % 2 == 0 else smaller_med
            return smaller_med + (bigger_med - smaller_med)*0.5
        
        elif left1 > right2:
            right = partition1 - 1
        else:
            left = partition1 + 1

if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    print(findMedianSortedArrays(nums1, nums2))



    """
    nums = [nums1, nums2]
    ids = [0, 0]
    curr, prev = None, None
    median_index = (len(nums1) + len(nums2)) // 2
    for i in range(median_index + 1):
        v1, v2 = [
            nums[i][ids[i]] if ids[i] < len(nums[i]) else float('inf')
            for i in [0, 1]
        ]
        if v1==float('inf') and v2==float('inf'):
            return 0.0
        if v1 < v2:
            ids[0] += 1
            prev = curr
            curr = v1
        else:
            ids[1] += 1
            prev = curr
            curr = v2


    bigger_median = curr
    smallr_median = prev if (len(nums1) + len(nums2)) % 2 == 0 else curr
    return float(smallr_median or 0) + (bigger_median - smallr_median or 0) * 0.5
    """
    
        


        