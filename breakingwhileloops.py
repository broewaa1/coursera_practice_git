#causes a infinite loop


#should print 1 2 3 4 5 
def print_range(start, end):
    # loop through the numbers from start to end
    #print the numbers from "1 2 3 4 5"
    n = start
    while n<=end:
        print(n)
        n += 1 # if you don't add this line, it will be an infinite loop
        #because the value of n will never change
        #print the numbers from "1 2 3 4 5"
        #need to pay attention to the condition of the while loop
        # if the condition is always true, it will be an infinite loop
print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)