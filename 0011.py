def maxArea(height: list[int]) -> int:
    max_water = 0
    r = len(height) - 1
    l = 0
    while (l < r) : 
        water = (r - l) * min(height[r], height[l]) 
        max_water = max(max_water, water)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return max_water

if __name__ == "__main__":
    assert maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert maxArea([1,1]) == 1
