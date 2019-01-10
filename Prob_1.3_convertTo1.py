"""
Prob 1-3 convertTo1
find how many calculate need to make number 1.
"""
def convertTo1(num):
    """
    convertTo1(x) = 'minimum count to be 1'
    
    convertTo1(n) = convertTo1(n/3) + 1 (n % 3 == 0)
    convertTo1(n) = convertTo1(n/2) + 1 (n % 2 == 0)
    convertTo1(n) = convertTo1(n-1) + 1
    
    Dynamic programming
    Bottom up
    from 1 to num
    
    """
    
    M = [num] * (num+1)
    M[1] = 0
    for i in range(2, num + 1):
        """
        M[i] is the Minimum result among three cases.
        Need to calculate ALL kinds of possible cases in three
        i.e. if i == 6, calculate all three cases
            M[i//3] + 1
            M[i//2] + 1
            M[i-1] + 1
        and find minimum value among them.
        
        => that's why
        if
            <calculate 1>
        if
            <calculate 2>
        <calculate 3>
        
        not
        if
            <calculate 1>
        elif
            <calculate 2>
        else
            <calculate 3>
        """
        
        # if i = 3k
        if (i % 3 == 0):
            M[i] = M[i//3] + 1
        
        # if i = 2k
        if (i % 2 == 0):
            M[i] = min(M[i], (M[i//2] + 1)) # 위의 것과 비교
        
        # etc
        M[i] = min(M[i], (M[i-1] + 1))  # 위의 것과 비교
        
    return M[num]


def convertTo1_1(num):
    
    values_past = [1]
    values = []
    M = [None]*num
    
    def func(x):
        if (x == 0 or x == 1):
            return 0
        
        elif (x == 2):
            return 1
        
        else:
            y = [x+1, x*2, x*3]
        return y
    
    if (M[num-1] != None):
        return M[num-1]
    
    else: 
        count = 0
        loop_stop = 1
        while(loop_stop):
            # Calculate values
            for val in values_past:
                output = func(val)
                for i in output:
                    values.append(i)

            # Check count
            count += 1

            # Check matching
            for i in values:
                if i == num:
                    loop_stop = 0

            # Update value list
            values_past = values
            values = []

        # Save count in array
        M[num-1] = count
    return count, M

def main():
    print(convertTo1(10))

if __name__ == "__main__":
    main()
