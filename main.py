# function that takes integer as input and returns the total sum of the digits of the integer
def digital_root(n):
    # variable to keep track of sum
    num = 0
    
    # recursive statement's base condition
    if n < 10:
        return n
    else:
        # split the integers into a list
        result = [int(i) for i in str(n)]
        
        # iterate over list, convert back to int from str 
        for i in result:
            num += int(i)
        
        # send back through the recursive function until condition met
        return digital_root(num)
