import turtle

t = turtle.Turtle()


def binary_tree(depth, length):
    ''' Takes two parameters: depth is the amount of recursions to
    compute and length which is the length of each branch of the
    tree. Prints a binary tree to the screen.
    '''
    
    if depth <= 0:
        return

    t.left(60)
    t.forward(length)
    t.right(60)
    binary_tree(depth - 1, length/2)  # recursion

    t.left(60)
    t.backward(length)

    t.right(120)
    t.forward(length)
    t.left(60)
    binary_tree(depth-1, length/2)   # recursion

    t.right(60)
    t.backward(length)
    t.left(60)

    return


def power(x, n):
    ''' Calculates the value x rasied to the exponent n.
    Has 2 preconditions that check if n is 0 which will
    return 1 and if n is negative an error message is printed
    and None is returned. 
    '''
    
    if(n<0): return
    if(n == 0): return 1
    
    temp = power(x, n//2) 
	 
    if (n % 2 == 0): return temp * temp    
    else: return x * temp * temp

def test_power():
    ''' Tests whether the power function works properly.
    Finds two different tests results based on built in power
    function and compares with user created function using recursion.
    Tests whether base case works properly.
    '''
    
    test_name = "test_power"
    test_base = 1
    test_2_8 = 2**8
    test_6_9 = 6**9
    
    try:
        base = (test_base == power(1,0))
        test1 = (test_2_8 == power(2,8))
        test2 = (test_6_9 == power(6,9))
        cond = (base == test1 == test2)
        return testif(cond, test_name, "WOO!", "boo...")
    except Exception as exc:
        print("test {} failed due to exception: {}\n".format(test_name, str(exc)))
        return False
       

def sum_slice(lst, begin, end):
    ''' Calculates the sum of a list recursively. Is passed
    a list of numbers, begin points to where to start in the
    list and end marks the end of the list to add. Creates a
    base_case list to check if base case is met.
    '''
    
    if begin < 0 or end > len(lst): raise IndexError
    if begin == end: return 0
    return lst[begin] + sum_slice(lst, begin+1, end)
    
    
def sum_slice_m(lst, begin, end):
    ''' Calculates the sum of a list recursively. Is passed
    a list of numbers, begin points to where to start in the
    list and end marks the end of the list to add. Creates a
    base_case list to check if base case is met. Uses memoization
    to store previous results in order to speed up processing time.
    '''
    
    if begin < 0 or end > len(lst): raise IndexError
    if begin == end: return 0
    if (begin,end) not in sum_dict:
        sum_dict[(begin,end)] = lst[begin] + sum_slice_m(lst, begin+1, end)
    return sum_dict[(begin,end)]  


sum_dict = {}   

    
def test_sum_slice():
    ''' Tests whether the sum_slice method functions properly.
    Finds the results of summing 2 different instances using a built
    in function and compares it with the results from the tested
    function. Tests the base case to check if it equals 0 and checks
    if precondition works properly requiring begin and end to be within
    the index of a list.
    '''
    
    lst = [1,2,3,4]
    test_name = "test_sum_slice"
    test_0_4 = sum(lst[0:4])
    test_1_3 = sum(lst[1:3])
    test_base = 0
    
    try:
        base = (test_base == sum_slice(lst,0,0))
        test1 = (test_0_4 == sum_slice(lst,0,4))
        test2 = (test_1_3 == sum_slice(lst,1,3))
        
        try: sum_slice(lst,-1,5)
        except IndexError: pre = True
        
        cond = (base == test1 == test2 == pre)
        return testif(cond, test_name, "WOO!", "boo...")
    
    except Exception as exc:
        print("test {} failed due to exception: {}\n".format(test_name, str(exc)))
        return False


def test_sum_slice_m():
    ''' Tests whether the sum_slice_m method functions properly.
    Finds the results of summing 2 different instances using a built
    in function and compares it with the results from the tested
    function. Tests the base case to check if it equals 0 and checks
    if precondition works properly requiring begin and end to be within
    the index of a list. Checks if result was properly stored in cache.
    '''
    
    lst = [1,2,3,4]
    test_name = "test_sum_slice_m"
    test_0_4 = sum(lst[0:4])
    test_1_4 = sum(lst[1:4])
    test_base = 0
    
    try:
        base = (test_base == sum_slice_m(lst,0,0))
        test1 = (test_0_4 == sum_slice_m(lst,0,4))
        test2 = (test_1_4 == sum_slice_m(lst,1,4))
        
        try: sum_slice_m(lst,-1,5)
        except IndexError: pre = True
        
        memoi = (sum_slice_m(lst,0,2) == sum_dict[(0,2)])
        
        cond = (base == test1 == test2 == pre == memoi)
        return testif(cond, test_name, "WOO!", "boo...")
    
    except Exception as exc:
        print("test {} failed due to exception: {}\n".format(test_name, str(exc)))
        return False


def testif(b, testname, msgOK="", msgFailed=""):
    ''' Function used for testing.
    param b: boolean, normally a tested condition: true if test passed, false otherwise
    param testname: the test name
    param msgOK: string to be printed if param b==True ( test condition )
    param msgFailed: string to be printed if param b==False ( test condition false )
    returns b
    '''
    if b: print("Success: " + testname + "; " + msgOK)
    else: print("Failed: " + testname + "; " + msgFailed)
    return b


def main():
    
    t.right(90)
    binary_tree(6, 160)
    turtle.done()
    
    print(power(2, 20))
    test_power()
    
    nums = [1,2,3,4]
    print("sum:", sum_slice(nums, 0, 4))
    print("sum:", sum_slice_m(nums, 0, 4))
    test_sum_slice()
    test_sum_slice_m()
    

if __name__ == "__main__":
    main()