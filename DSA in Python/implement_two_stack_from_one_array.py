#User function Template for python3


#Function to push an integer into the stack1.
def push1(a,x):
    #code here
    global top1 # Global to Access local variable
    top1 = top1 + 1
    a[top1] = x
    
#Function to push an integer into the stack2.
def push2(a,x):
    #code here
    global top2
    top2 = top2 - 1
    a[top2] = x
    
#Function to remove an element from top of the stack1.    
def pop1(a):
    #code here
    global top1
    if top1==-1:
        return -1
    else:
        temp = a[top1]
        top1 = top1 - 1
        return temp
        
        
    
#Function to remove an element from top of the stack2.    
def pop2(a):
    #code here
    global top2
    if top2>=101:
        return -1
    else:
        temp = a[top2]
        top2 = top2 + 1
        return temp
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

top2=101
top1=-1

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arr = list(map(int,input().strip().split()))
        a = [-1 for i in range(101)] # array to be used for the 2 stacks.
        i=0 # curr index
        while i<len(arr):
            if arr[i] == 1:
                if arr[i+1] == 1:
                    push1(a,arr[i+2])
                    i+=1
                else:
                    print(pop1(a),end=" ")
                i+=1
            else:
                if arr[i+1] == 1:
                    push2(a,arr[i+2])
                    i+=1
                else:
                   print(pop2(a),end=" ")
                i+=1
            i+=1
        top2=101
        top1=-1
        print(' ')

# } Driver Code Ends