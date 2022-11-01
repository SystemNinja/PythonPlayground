
def InsertionSort(array):
    for i in range(1,len(array)):
        #using first element of the array as key then comparing it with other values until smaller value is found, 
        #that value becomes new key
        key=array[i] 
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j=i-1
        while j >=0 and key < array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key
    

array=[1,3,10,5,7,23,11,30,2,35]
InsertionSort(array)
print("Sorted array is:")
for i in range(len(array)):
    print(array[i])