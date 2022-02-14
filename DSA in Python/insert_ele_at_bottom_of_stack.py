
def insert_at_bottom(stack, ele):
    temp = []
    while stack:
        temp.append(stack[-1])
        stack.pop()
    temp.append(ele)
    while temp:
        stack.append(temp[-1])
        temp.pop()
    return stack
    


if __name__== "__main__":
    stack = []
    stack.append(1)
    stack.append(3)
    stack.append(5)
    stack.append(7)
    stack.append(4)
    print("Original Stack:", stack)
    ins = int(input("\nEnter the element you want to insert at the bottom: "))
    print("\nAfter inserting {} at bottom".format(ins), insert_at_bottom(stack,ins))


