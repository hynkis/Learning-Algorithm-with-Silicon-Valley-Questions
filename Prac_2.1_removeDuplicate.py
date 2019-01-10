"""
Prac. 2-1 removeDuplicate
중복된 수 제거하기
0보다 큰 정수들이 있는 리스트가 주어집니다. 이 리스트는 작은것부터 큰 순서대로 오름차순 정렬이 되어있으며, 중복을 포함합니다. 이 리스트에서 중복된 수를 없애고 정렬되어있는 리스트를 출력해 봅시다.

예를 들어 [1, 1, 2, 2, 2, 2, 5, 7, 7, 8] 이 입력되었다면 중복되어있는 ‘1’ 1개, ‘2’ 3개, ‘7’ 1개를 제거하고 [1, 2, 5, 7, 8]을 출력하면 됩니다.
"""

def removeDuplicate(nums):
    result = []
    result.append(nums[0])
    for ind in range(1, len(nums)):
        if nums[ind] == nums[ind-1]:
            continue
        result.append(nums[ind])
    return result

def main():
    print(removeDuplicate([1, 1, 2, 2, 2, 2, 5, 7, 7, 8])) # [1, 2, 5, 7, 8]을 리턴해야 합니다

if __name__ == "__main__":
    main()
