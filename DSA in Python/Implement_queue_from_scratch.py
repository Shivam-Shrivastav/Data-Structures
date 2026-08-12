#User function Template for python3

class MyQueue:
    
    def __init__(self):
        self.arr = []
        self.front = 0
        self.rear = 0

    # Queue operates on FIFO template
    # Therefore firstly we append the queue and from there a real life queue will be made by push operation
    # i.e 2 will come after 1, 3 will come after 2 and so on
    # And since on in a queue first man/person is considered first therefore, will return the first element in the list
    # then will move the front pointer to the next guy i.e 2nd guy and so on
    
    #Function to push an element x in a queue.
    def push(self, x):
        self.arr.append(x)
        self.rear = self.rear + 1
     
    #Function to pop an element from queue and return that element.
    def pop(self):
        if self.front == self.rear:
            return -1
        elif self.front < self.rear:
            temp = self.arr[self.front]
            self.front = self.front + 1
        return temp
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   

# } Driver Code Ends