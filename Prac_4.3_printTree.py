"""
이진 트리 출력하기
완벽한 이진 트리가 주어졌다고 합시다. 이때, 이 트리를 출력하기 좋은 형태로 반환하는 함수를 구현 해 봅시다. 위에서부터 순서대로, 트리의 각 층별로 하나의 배열을 만들고, 이 배열들의 배열을 반환하는 형태면 됩니다.

예를 들어서

 1
2 3

Copy
와 같은 트리가 주어졌을 경우 [[1],[2,3]] 을,

   1
 2   3
4 5 6  7

Copy
과 같은 트리가 주어졌을 경우에는 [[1],[2,3],[4,5,6,7]]을 반환하면 됩니다.
"""

import queue

#====이 문제를 풀기 위해 필요한 클래스와 함수들입니다. 따로 수정 할 필요는 없습니다.
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def listToCompleteBinaryTree(lst):
    def helper(index):
        if index >= len(lst):
            return None
        node = Node(lst[index])
        node.left = helper(index * 2 + 1)
        node.right = helper(index * 2 + 2)
        return node
    return helper(0)
#=================================================================================
"""
def printTree(node):
    all_lines = []
    return all_lines
"""
def printTree(node):
    all_lines = []
    line = []
    q = queue.Queue()
    
    # queue에 root값 입력
    q.put(node)
    q.put(Node(-1)) # 전체 node의 깊이를 구분하기 위한 구분자 추가.
    
    # queue size가 0이 아닌 이상 계속 수행
    while q.qsize() > 0:
        temp_node = q.get()
        
        # 이때 q에서 나오는 값이 있으면 진행
        if temp_node:
            # 구분자인 -1이 나오면 line에 저장된 값들을 all_lines에 입력
            # 그 후 line 초기화 및 -1을 q에 입력
            if temp_node.val == -1:
                all_lines.append(line)
                line = []
                q.put(Node(-1))
            # 구분자 외의 node의 경우
            # line에 값 추가 및 q에 node의 left, right 추가
            else:
                line.append(temp_node.val)
                q.put(temp_node.left)
                q.put(temp_node.right)
        
        # 나온 값이 None인 경우(4567의 다음 숫자가 없으므로 None 나온다)
        else:
            break # 중단하여 all_lines 출력
            
        
    return all_lines

def main():
    node = listToCompleteBinaryTree([1,2,3,4,5,6,7])
    print(printTree(node)) # [[1], [2, 3], [4, 5, 6, 7]]

if __name__ == "__main__":
    main()
    
