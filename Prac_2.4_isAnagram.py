"""
Prac. 2-4 isAnagram

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
