"""
피보나치 수
피보나치 수열은 N 번째 수가 N-1번째 수와 N-2번째 수의 합인 수열입니다. 즉, F(0) = 0, F(1) = 1이며 그 이외의 모든 F(n) = F(n-1) + F(n-2) 입니다.

예를 들어서 피보나치 수열을 0~ 10번째까지 적어보면

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

와 같습니다.

F(10) = F(9) + F(8) = 21 + 34 = 55 임을 확인 할 수 잇습니다.

0보다 크거나 같은 입력 정수 n이 주어졌을때 n번째 피보나치 수를 반환하는 함수를 구현 해 봅시다.

예를 들어서, 10이 입력으로 주어지면 55를 반환해야 합니다.

재귀 방법으로 구현 해 보도록 합시다. 메모이제이션도 활용 해 보도록 합시다.
"""

class Fib():
    def __init__(self):
        self.memo = {}

    def fibonacci(self, num):

        # base condition
        if num == 0:
            return 0
        elif num == 1:
            return 1
        
        # [DP] dictionary에 key 있으면 바로 return
        if num in self.memo:
            return self.memo[num]
            
        # main fibonacci function
        else:
            self.memo[num] = self.fibonacci(num - 2) + self.fibonacci(num - 1)
            return self.memo[num]
        
def main():
    fib = Fib()
    print(fib.fibonacci(10)) # should return 55

"""
class Fib():
    def __init__(self):
        self.memo = {}

    def fibonacci(self, num):
        return 0
        
def main():
    print(fibonacci(10)) # should return 55
"""

if __name__ == "__main__":
    main()
