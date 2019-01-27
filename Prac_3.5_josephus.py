"""
조세퍼스 순열
입력으로 두 숫자가 들어오면 조세퍼스 순열을 구하는 함수를 작성해 봅시다.

조세퍼스 순열이 무엇인가 어렵게 느껴지지만 알고보면 쉽습니다.

사람이 7명이 둘러 앉아 있다고 생각해 봅시다. (캠프파이어를 상상해 보세요.) 이때 3번째 사람이 나갑니다. 그후 그 다음 3번째 사람이 나가고 다음 3번째 사람이 나가는 것을 모두가 나갈 때가지 반복해봅시다. 그러면 차례대로 3, 6, 2, 7, 5, 1, 4번째 사람이 나가게 될 것입니다.

이때 사람이 나간 순서가 7, 3의 조세퍼스 순열입니다.

Hint
큐를 사용해 보세요!
"""

import queue

def josephus(num, target):
    result = []
    
    # queue를 채운다.
    q = queue.Queue()
    for i in range(1, num+1):
        q.put(i)
        
    i = 1
    while True:
        # i가 3의 배수일 때 queue에서 get하여 result에 저장.
        # 그후 i는 1로 reset.
        if i % target == 0:
            result.append(q.get())
            i = 1
            
        # 그 외에는 선두의 숫자를 get해서 후미에 넣는다.
        # i는 늘려준다.
        else:
            q.put(q.get())
            i += 1
            
        # queue가 비면 종료
        if q.qsize() == 0:
            return result
        
        
            
def main():
    print(josephus(7, 3)) #[3, 6, 2, 7, 5, 1, 4]이 반환되어야 합니다

if __name__ == "__main__":
    main()
