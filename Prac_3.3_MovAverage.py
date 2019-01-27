"""
스트리밍 데이터의 이동 평균
정수 데이터가 스트리밍으로 (한번에 하나씩) 주어진다고 합시다. 이때, 주어진 범위 만큼의 이동 평균을 구하는 클래스 MovingAvg를 만들어 봅시다.

MovingAvg는 처음에 이동 평균의 범위를 입력받아서 초기화 되며, 매 정수 데이타가 입력되는 nextVal(num)함수는 이때까지의 이동 평균을 반환합니다.

예를 들어서, 2,8,19,37,4,5 의 순서로 데이터가 입력되고, 이동 평균의 범위는 3이라고 합시다. 이 경우 다음과 같이 MovingAvg가 사용 될 것입니다.
"""

import queue

class MovingAvg():
    def __init__(self, size):
    
        self.q = queue.Queue()
        self.sum = 0
        self.size = size

    def nextVal(self, num):
        
        # size 값만큼 queue가 쌓이면 기존의 값들을 빼내준다.
        # 누적값 sum에도 빼진 값들 반영.
        if self.q.qsize() == self.size:
            self.sum -= self.q.get()
        
        # 새로 들어온 값을 넣는다.
        self.q.put(num)
        self.sum += num

        return self.sum / self.q.qsize()

def queueExample():
    q = queue.Queue()
    q.put(1)
    q.put(2)
    print(q.qsize())
    print(q.get())
    print(q.qsize())
    print(q.get())
    
def main():
    # queueExample()

    nums = [2,8,19,37,4,5]
    ma = MovingAvg(3)
    results = []
    for num in nums:
        avg = ma.nextVal(num)
        results.append(avg)
    print(results) # [2.0, 5.0, 9.666666666666666, 21.333333333333332, 20.0, 15.333333333333334]
if __name__ == "__main__":
    main()
