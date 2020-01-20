import math
def generateNoConsicutiveOne(val, arr, i):
    # print binary string without consecutive 1's 
    #for i in range(0, val):
    if (i == val): 
        # terminate binary string 
            #arr[i] = [None]*val 
            print (arr)
            return 
  
    # if previous character is '1' then we put 
    # only 0 at end of string 
    #example str = "01" then new string be "000" 
    if (arr[i-1] == 1): 
        arr[i] = 0
        generateNoConsicutiveOne(val , arr , i+1)
  
    # if previous character is '0' than we put 
    # both '1' and '0' at end of string 
    # example str = "00" then new  string "001" and "000" 
    if (arr[i-1] == 0): 
        arr[i] = 0 
        generateNoConsicutiveOne(val, arr, i+1)
        arr[i] = 1
        generateNoConsicutiveOne(val, arr, i+1)

# function generate all binary string without 
# consecutive 1's 


   # Function to generate all binary strings  
def generateAllBinaryStrings(val, arr, i):  
  
    # First assign "0" at ith position  
    # and try for all other permutations  
    # for remaining positions  
    arr[i] = 0
    generateNoConsicutiveOne(val, arr, i + 1)  
  
    # And then assign "1" at ith position  
    # and try for all other permutations  
    # for remaining positions  
    arr[i] = 1
    generateNoConsicutiveOne(val, arr, i + 1)  
  
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
