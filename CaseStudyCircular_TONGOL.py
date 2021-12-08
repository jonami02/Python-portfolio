##TONGOL, JOMINA SOPHIA B.
##CS202

print("\nTHE LIMIT OF OUR QUEUES IS 10\n")

def main():
    print("Operations: ")
    print("[1] Circular ")
    print("[2] Priority ")
    print("[3] Quit ")

def circularOperation():
    print("\nCircular Operations: ")
    print("[1] Enqueue Element ")
    print("[2] Dequeue Element ")
    print("[3] back to main ")
    

class CircularQueue(): 
  
    # constructor 
    def __init__(self, size): # initializing the class 
        self.size = size 
          
        # initializing queue with none 
        self.queue = [None for i in range(size)]  
        self.front = self.rear = -1
  
    def enqueue(self, data): 
          
        # condition if queue is full 
        if ((self.rear + 1) % self.size == self.front):  
            print(" Queue is Full\n") 
              
        # condition for empty queue 
        elif (self.front == -1):  
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data 
        else: 
              
            # next position of rear 
            self.rear = (self.rear + 1) % self.size  
            self.queue[self.rear] = data
        
              
    def dequeue(self): 
        if (self.front == -1): # codition for empty queue 
            print ("Queue is Empty\n") 
              
        # condition for only one element 
        elif (self.front == self.rear):  
            temp=self.queue[self.front] 
            self.front = -1
            self.rear = -1
            return temp 
        else: 
            temp = self.queue[self.front] 
            self.front = (self.front + 1) % self.size 
            return temp 
  
    def display(self): 
      
        # condition for empty queue 
        if(self.front == -1):  
            print ("Queue is Empty") 
  
        elif (self.rear >= self.front): 
            print("Elements in the circular queue are:",  
                                              end = " ") 
            for i in range(self.front, self.rear + 1): 
                print(self.queue[i], end = " ") 
            print ()
            print("Front is: ", self.front)
            print("Rear is: ", self.rear)
  
        else: 
            print ("Elements in Circular Queue are:",  
                                           end = " ") 
            for i in range(self.front, self.size): 
                print(self.queue[i], end = " ") 
            for i in range(0, self.rear + 1): 
                print(self.queue[i], end = " ") 
            print ()
            print("Front is: ", self.front)
            print("Rear is: ", self.rear)
  
        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full and index", end=" ")
            for i in range(self.front, self.size):
                if self.queue[i] is None:
                    print(i, end=",")
            print(" is NONE ")
                

    def pEnque(self, data, index):
        self.index = index


        if (self.front == -1):  
            self.front = 0
            self.rear = index
            self.queue[self.rear] = data
        
        elif(self.queue[self.index] is not None):
             print("\nINDEX IS ALREADY FILLED!!\n")

        elif (self.queue[self.rear] is None):
              self.queue[self.rear] = data
        
        # condition for empty queue 

        elif  (self.index < self.rear):
            self.queue[self.index] = data
        

        elif (self.queue[self.rear] is None):
              self.queue[self.rear] = data
              
        else: 
              
            # next position of rear 
            self.rear = index  
            self.queue[self.rear] = data
        
        

circular = CircularQueue(10)
while True:
    global choice
    try:
        main()
        choice = int(input("Enter choice[1-3]: "))
        if choice == 1:
            circularOperation()
            choice2 = int(input("Enter choice[1-3]: "))

            if choice2 == 1:
                element= int(input("Enque element: "))
                circular.enqueue(element)
                circular.display()
                answer=input("\nEnque another element[y/n]?: ")
                while answer in 'yY':
                    element= int(input("Enque element: "))
                    circular.enqueue(element)
                    circular.display()
                    answer=input("\nEnque another element[y/n]?: ")

            elif choice2 == 2:
                circular.dequeue()
                circular.display()
                answer=input("\nDequeue another element[y/n]?: ")
                while answer in 'yY':
                    circular.dequeue()
                    circular.display()
                    answer=input("\nDequeue another element[y/n]?: ")

            elif choice2 >=4:
                print("\nChoices are 1-3 only!\n")
                
            else:
                continue
                
                    
        elif choice == 2:
            index = int(input("Input index: "))
            if (index <= 9) :
                element= int(input("Enque element: "))
                circular.pEnque(element, index)
                circular.display()
                answer=input("\nEnque another element[y/n]?: ")
                while answer in 'yY':
                    index = int(input("Input index: "))
                    if (index <= 9) :
                        element= int(input("Enque element: "))
                        circular.pEnque(element, index)
                        circular.display()
                        answer=input("\nEnque another element[y/n]?: ")
                    else:
                        print("\nINDEX 0-9 ONLY!\n")
            else:
                print("\nINDEX 0-9 ONLY!\n")
            
        elif choice == 3:
            ans = input("Are you sure you want to EXIT? Y/N ")
            if ans == "y" or ans == "Y":
                break
            else:
                continue

        else:
            print("\nChoices are 1-3 only!\n")
    except ValueError:print("\nInvalid Input!\n")
    


        


