"""
괄호 매칭
(, ), {, }, <, >, [, ] 의 여덟개의 문자로만 구성된 문자열이 입력으로 주어진다고 해 봅시다.

이때, 이 문자열이 유효한지를 확인하는 함수를 작성 해 보세요.

열린 괄호들이 닫히는 순서가 올바르게 되어 있는 경우에 그 문자열을 유효하다고 합니다.

즉, ({()}) 나 []<>{} 등은 유효한 문자열이며, )( <] <(>) 등은 유효하지 않은 문자열입니다.

“열린 순서대로 닫히는” 것을 어떻게 구현 할 수 있을지 고민 해 보세요.
"""

def isParenthesisValid(st):
    pOpen = ["(", "{", "<", "["]                            # open 문자
    pDict = { ")" : "(", "}" : "{", ">" : "<", "]" : "[" }  # closed 문자에 대응하는 open 문자
    stack = []
    
    for ch in st:
        # ch가 pOpen에 있는 문자인지 확인
        if ch in pOpen:
            stack.append(ch) # pOpen에 있으면 stack에 stack.
                    
        # ch가 pOpen에 있는 문자가 아닌 경우.
        else:
            # ch의 대칭되는 문자와 stack의 제일 윗 문자가 같으면 pop하고 다음으로. 다르면 무효.
            # stack의 길이가 0인 경우, 즉 closed만 있고 open이 없는 경우
            if len(stack) != 0 and stack[-1] == pDict[ch]:
                stack.pop()
                
            else:
                return False
    
    return True

def main():
    examples = ["({()})", "[]<>{}", ")(" "<]", "<(>)"]
    for example in examples:
        print(example, isParenthesisValid(example))

    
if __name__ == "__main__":
    main()
    
