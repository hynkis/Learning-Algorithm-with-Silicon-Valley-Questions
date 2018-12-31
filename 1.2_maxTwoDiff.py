def maxTwoDiff1(nums):
    """
    nums.sort() : O(NlogN)
    """
    nums.sort()
    return nums[-1] - nums[0]

def maxTwoDiff(nums):
    """
    max, min : O(N)
    """
    return max(nums) - min(nums)

def main():
    print(maxTwoDiff([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23])) # should return 49
    
if __name__ == "__main__":
    main()
