def main():
    numberofitems = int(input("Enter number of items >> "))
    stack = []
    top = 0
    supermax = numberofitems
    choice = "a"
    while choice != "x":
        printoptions()
        choice = input("Enter choice >> ")
        if choice == "a":
            if top < supermax:
                num = inputnum()
                stack.insert(top,num)
                top+=1
            else:
                print("Stack overflow")
            printstack(stack)
        elif choice == "b":
            if top > 0:
                stack.pop()
                top-=1
            else:
                print("Stack underflow")
            printstack(stack)
        elif choice == "c":
            print(stack[top-1])
            print("count = ",top)
def printoptions():
    print("[a] Push")
    print("[b] Pop")
    print("[c] Peek")
    print("[x] End")

def inputnum():
    num = int(input("Enter number to push >> "))
    return num

def printstack(stack):
    for i in range (len(stack)-1,-1,-1):
        print(stack[i])
main()
