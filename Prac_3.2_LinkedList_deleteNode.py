"""
연결 리스트에서 노드 삭제하기
연결 리스트가 주어지고, 이 연결리스트에서 삭제하고 싶은 노드의 값이 주어졌다고 해 봅시다.

연결 리스트를 순회하면서 해당 노드를 찾아서, 삭제하는 함수를 만들어 봅시다.

주어진 연결 리스트에서 직접 삭제를 시행하면 되기 때문에, 해당 연결 리스트를 반환 할 필요는 없습니다.
"""

# 연결 리스트의 노드. 단일 연결 리스트의 경우입니다.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def __str__(self):
        return str(self.val)

# 연결 리스트 클래스. head 와 tail을 가지고 있으며, 가장 뒤에 새로운 노드를 추가하는 addToEnd 함수가 있습니다.
class LinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head
    
    def addToEnd(self, node):
        self.tail.next = node
        self.tail = node
        
    def __str__(self):
        node = self.head
        toPrint = []
        while node:
            toPrint.append(str(node.val))
            node = node.next
        return "->".join(toPrint)

# 주어진 배열을 linkedlist로 변환해서 돌려줍니다. 실습 3-1을 참조하세요
def toLinkedList(lst):
    ll = LinkedList(Node(lst[0]))
    for i in range(1, len(lst)):
        ll.addToEnd(Node(lst[i]))
    
    return ll
    
####################################################################################################################################

def deleteNode(ll, valToDelete):
    
    if ll.head.val == valToDelete:
        ll.head = ll.head.next
    
    currNode = ll.head
    nextNode = currNode.next
    
    while nextNode: # nextNode가 None이 아니면 계속 loop 수행
        if nextNode.val == valToDelete:
            currNode.next = nextNode.next
            
            # 만일 지웠던 nextNode가 tail이었다면
            # ll의 tail을 현재 node로 바꿔주고 break.
            if nextNode == ll.tail:
                ll.tail = currNode
                break
            
        # currNode가 tail의 앞 node이라면
        # currNode는 tail로, nextNode는 None이 되어 while loop가 break 된다.
        # tail이 지워진 경우가 아니라면 마지막 node가 기존 ll의 tail로 계속 유지되는 것이기에
        # tail을 업데이트하지 않아도 된다.
        currNode = currNode.next
        nextNode = currNode.next
            

def main():
    nums = [2,8,19,37,4,5]
    ll = toLinkedList(nums)
    print(ll)
    deleteNode(ll, 19)
    print(ll) # 19를 삭제하였으므로, 2->8->37->4->5
    deleteNode(ll, 5)
    print(ll) # 3이 없으므로, 2->8->37->4->5

if __name__ == "__main__":
    main()
