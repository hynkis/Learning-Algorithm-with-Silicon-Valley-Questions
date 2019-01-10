"""
Prob 1-2 maxSubArray
Find maximun Sub sum from and Array
"""


def maxSubArray_memoryLess(nums):
    maxSum = 0
    tempSum = 0
    """
    maxSum would save maximum summation value until index i.
    
    """
    for i in range(len(nums)):
        if (tempSum + nums[i] > 0):
            tempSum = tempSum + nums[i]
        else:
            tempSum = 0
        if maxSum < tempSum:
            maxSum = tempSum
    return maxSum

def maxSubArray_DP(A):
    maxSum = 0
    M = [0]*len(A)  # initialize list
    
    # set M[0]
    if A[0] > 0:
        M[0] = A[0]
    else:
        M[0] = 0
    
    # calculate M[1] ~ M[l-1]
    for i in range(1, len(A)):
        """
        if M[i-1] + A[i] is positive, M[i] = M[i-1] + A[i].
        if M[i-1] + A[i] is negatice or zero i.e. A[i] < -M[i-1], make M[i] 0.
        because M[i] is the maximum summation value of all sub-arrays whose final index is i.
        """
        if (M[i-1] + A[i] > 0):
            M[i] = M[i-1] + A[i]
        else:
            M[i] = 0
            
        if maxSum < M[i]:
            maxSum = M[i]
    
    return maxSum
        

def maxSubArray2(nums):
    
    sum_list = []
    for i in range(len(nums)):
        # find positive value
        if nums[i] > 0:
            # check maximum sum of left side until index == 0
            left_max = 0
            sub_sum = nums[i]
            j = i - 1
            while(j >= 0):
                sub_sum = sub_sum + nums[j]
                j -= 1
                if left_max < sub_sum:
                    left_max = sub_sum

            # check maximum sum of right side until index == len(nums)-1
            right_max = 0
            sub_sum = nums[i]
            k = i + 1
            while(k < len(nums)):
                sub_sum = sub_sum + nums[k]
                k += 1
                if right_max < sub_sum:
                    right_max = sub_sum
            
            # find maximum value between left / right
            sum_list.append(max(left_max, right_max))
            
        else:
            continue
    
    # find maximum values between positive values
    return max(sum_list)


def maxSubArray1(nums):
    """ Sliding window method """
    sum_list = []
    
    for l in range(len(nums)): # l : length of window - 1
        sub_sum_list = []
        
        for i in range(len(nums) - l): # index range for searching
            """ summation of vals in a window """
            j = 0
            sum = nums[i]
            
            while(1):
                if (j == l): break  # while loop until j == length of window - 1
                j += 1
                sum = sum + nums[i + j]
                
            sub_sum_list.append(sum) # collect sub sum            
            
        sum_list.append(max(sub_sum_list)) # collect maximum of sub_sum_list
    
    return max(sum_list)



def main():
    print(maxSubArray_DP([-10, -7, 5, -7, 10, 5, -2, 17, -25, 1])) # 30이 리턴되어야 합니다

if __name__ == "__main__":
    main()
