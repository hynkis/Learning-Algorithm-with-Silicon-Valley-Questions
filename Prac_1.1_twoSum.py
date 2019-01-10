def twoSum1(nums, target):   # for for => O(n^2)
    for num1 in nums:
        if target == num1 + num2:
            return num1, num2
        
def twoSum2(nums, target):   # for for => O(n^2)
    for n in nums: # O(n)
        if (target - n) in nums:  # O(n)
            return n, (target - n)
        
def twoSum(nums, target):
    nums.sort()      # sort list(nums) ascending.
    i = 0              # from 1st val in list.
    j = len(nums) - 1  # from last val in list.
    while i < j:
        sum = nums[i] + nums[j]
        if sum > target:     # if sum > target => make nums[j] lower
            j -= 1
        elif sum < target:   # if sum < target => make nums[i] higher
            i += 1
        else:
            break
    return nums[i], nums[j]
        
def main():
    print(twoSum([2, 8, 19, 37, 4, 5], 12)
    
if __name__ == "__main__":
          main()
