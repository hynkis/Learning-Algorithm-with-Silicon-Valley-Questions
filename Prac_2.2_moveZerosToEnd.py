"""
Prac. 2-2 moveZerosToEnd
0 이동시키기
여러개의 0과 양의 정수들이 섞여 있는 배열이 주어졌다고 합시다. 이 배열에서 0들은 전부 뒤로 빼내고, 나머지 숫자들의 순서는 그대로 유지한 배열을 반환하는 함수를 만들어 봅시다.

예를 들어서, [0, 8, 0, 37, 4, 5, 0, 50, 0, 34, 0, 0] 가 입력으로 주어졌을 경우 [8, 37, 4, 5, 50, 34, 0, 0, 0, 0, 0, 0] 을 반환하면 됩니다.

이 문제는 공간 복잡도를 고려하면서 풀어 보도록 합시다. 공간 복잡도 O(1)으로 이 문제를 풀 수 있을까요?
"""

def moveZerosToEnd(nums):
    # currentPosition for inserting a non-zero value
    currentPosition = 0
    # check each value in nums
    for i in range(len(nums)):
        # if the value is not 0,
        if nums[i] != 0:
            # insert the value to nums[currentPosition]
            nums[currentPosition] = nums[i]
            # check currentPosition == i.
            # 같은 경우 currentPosition에 non-zero값을 넣은 것이므로 0으로 만들면 안된다.
            if i != currentPosition:
                nums[i] = 0
            # update currentPosition
            currentPosition += 1            
            
    return nums

def moveZerosToEnd1(nums):
    # Check each number in nums
    for i in range(len(nums)):
        # if num[i] is 0, pass
        if nums[i] == 0:
            continue
        # if num[i] is not 0,
        else:
            # if index is 0, break
            if i == 0:
                break
            # if index is not 0, check prior index
            else:
                j = i
                # if prior number is 0, pass
                while nums[j-1] == 0:
                    j -= 1
                    # if next j is 0, break (Should not be -1 index)
                    if j == 0:
                        break
            # if prior number(nums[j-1]) is not 0,
            # insert current number(nums[i]) in nums[j]
            nums[j] = nums[i]
            # change current number to 0
            nums[i] = 0
            
    return nums

def main():
    print(moveZerosToEnd([0, 8, 0, 37, 4, 5, 0, 50, 0, 34, 0, 0]))

if __name__ == "__main__":
    main()
