"""
Prac. 2-4 isAnagram

아나그램 탐지
아나그램(Anagram)은 한 문자열의 문자를 재배열해서 다른 뜻을 가지는 다른 단어로 바꾸는 것을 의미합니다.

두 개의 문자열이 주어졌을 때, 서로가 서로의 아나그램인지 아닌지의 여부를 탐지하는 함수를 만들어 보세요.

"""

def isAnagram(str1, str2):
    # dictionary M
    M = dict()
    # insert each charactor in string1
    for char in str1:
        M[char] = M.get(char, 0) + 1
    
    # check whether each charactor is in dict M
    for char in str2:
        # if it is, pass
        if char in M:
            continue
        # if it isn't, return False
        else:
            return False
    # if all charactors are in strs, return True
    return True

def main():
    print(isAnagram('iamlordvoldemort', 'tommarvoloriddle')) # should return True
    print(isAnagram('cat', 'cap')) #should return False
    

if __name__ == "__main__":
    main()
