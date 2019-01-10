"""
Prob 1-1 findDuplicate
Find the value which is duplicate.
"""

def findDuplicate(nums):
    nums.sort()
    i = 0
    while(1):
        if (nums[i] == nums[i+1]):
            break
        else:
            i += 1
    
    return nums[i]

def main():
    print(findDuplicate([1, 5, 2, 4, 5, 6, 3]))

if __name__ == "__main__":
    main()
