# Python program for implementation of Insertion Sort 
  
# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
        print(arr)
        key = arr[i]
        print("key is: ", key)
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        print("j is: ", j)

        while j >= 0 and key < arr[j] :
                print("j >= 0* ", j , " and key* ", key , " < arr[j]* ", arr[j]) 
                arr[j + 1] = arr[j]
                print("arr[j+1] is now: ", arr[ j + 1])
                j -= 1
                print("j now is: ", j)
                print(arr)
                print()
        arr[j + 1] = key
        print("outside loop arr[j+1] is: ",arr[j+1]," and key is: ",key )
        print("arr[j] ", arr[j])
        print(arr)
        print("*****************")
  
  
# Driver code to test above 
arr = ["x","s","n","a","e","j","o","m","l","f"] 
insertionSort(arr) 
for i in range(len(arr)): 
    print (arr[i])
