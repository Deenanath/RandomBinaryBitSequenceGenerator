import math

def generateAllBinaryStrings(val, arr, i):  
    DNGSWrite=open("DNGSWrite.txt","a")    
    if i == val:
        for j in range(val):
            if arr[j]==0:
                arr[j]=-1
        s=0
        for k in range(val):
            s=s+arr[k]
        if (s==0):
            print (arr, end="", file=DNGSWrite)
        return
    print(file=DNGSWrite)
        # writeTheArray(arr,val)
        
    DNGSWrite.close()     
    # First assign "0" at ith position  
    # and try for all other permutations  
    # for remaining positions  
    arr[i] = 0
    generateAllBinaryStrings(val, arr, i + 1)  
 
    # And then assign "1" at ith position  
    # and try for all other permutations  
    # for remaining positions  
    arr[i] = 1
    generateAllBinaryStrings(val, arr, i + 1)  
 
# Driver Code  
if __name__ == "__main__":  
 
    print("enter the value for n")
    n = input("Enter your value: ")
    val1=int(n)
    m=math.pow(2,val1)
    val=int(m)
    print("Number of bit length generation will be :-",val)
    #n = 5
    arr = [None] * val  
    
    # Print all binary strings  
    generateAllBinaryStrings(val, arr, 0)

