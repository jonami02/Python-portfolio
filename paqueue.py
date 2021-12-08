def main():
    numberofitems = int(input("Enter number of items >> "))
    q = []
    top = 0
    supermax = numberofitems
    count = 0
    front = 0
    rear = 0
    back = 0
    choice = "a"
    while choice != "x":
        printoptions()
        choice = input("Enter choice >> ")
        if choice == "a":
            if count < numberofitems:
                num = inputnum()
                q.insert(top,num)
                top+=1
                rear += 1
                back += 1
                count += 1
            else:
                print("Stack overflow")
            printstack(q)
        elif choice == "b":
            if top > 0:
                del q[0]
                front += 1
                back -= 1
                top-=1
            else:
                print("Stack underflow")
            printstack(q)
        elif choice == "c":
            print(front)
            print("front = ",q[0])
        elif choice == "d":
            print(rear-1)
            print("rear = ",q[back-1])
def printoptions():
    print("[a] Enqueue")
    print("[b] Dequeue")
    print("[c] Front")
    print("[d] Rear")
    print("[x] End")

def inputnum():
    num = int(input("Enter number to push >> "))
    return num

def printstack(q):
    print(q)
main()
