"""
스택 수열
스택에 1부터 N까지 차례대로 넣었다가 뽑아 리스트에 넣습니다. 이때 모두 넣은뒤 모두 뽑는것이 아닌 넣는 과정과 뽑는 과정을 섞어서 진행할 수도 있습니다. 이때 만들어진 수열을 스택 수열이라고 합시다.

1부터 N까지의 수로 이루어진 리스트가 주어집니다. 이때 이 리스트가 스택수열인지 검사하는 함수를 만들어 봅시다.

예를 들어 [2, 1, 4, 3]은 스택 수열입니다. 1넣기 -> 2넣기 -> 2뽑기 -> 1뽑기 -> 3넣기 -> 4넣기 -> 4뽑기 ->3뽑기 의 과정을 거치면 만들어 질 수 있기 때문입니다.

그러나 [3, 1, 2, 4]는 스택 수열이 아닙니다. 위에 나온 스택수열을 만드는 방법으로는 어떻게 해도 만들 수 없기 때문입니다.
"""

def isStackSequence(nums):
    n = 1
    tempStack = []
    resultStack = []
    
    i = 0
    
    while True:
        # 1. n 값이 nums[i]보다 작으면 temp에 stack
        if n < nums[i]:
            tempStack.append(n)
            # 그 다음의 n값에 대해 판단. (i는 그대로)
            n += 1
            
        # 2. n 값이 nums[i]보다 크면 tempStack의 값을 pop하여 result로 stack
        elif n > nums[i]:
            # tempStack에 아무것도 없으면 유효하지 않으므로 False.
            if len(tempStack) == 0:
                return False
            # 있으면 pop하여 result에 stack
            # 이때 nums[i]와 같은 값이 pop되었다면 인덱스 i 업뎃 
            else:
                popVal = tempStack.pop()
                resultStack.append(popVal)
                
                if popVal == nums[i]:
                    i += 1
                    
        # 3. n == nums[i]이면 바로 result에 stack.
        else:
            resultStack.append(n)
            n += 1
            i += 1
            
        if i == len(nums): break
                
    return True

def main():
    print(isStackSequence([2, 1, 4, 3])) # True가 리턴되어야 합니다
    print(isStackSequence([3, 1, 2, 4])) # False가 리턴되어야 합니다

    
if __name__ == "__main__":
    main()
