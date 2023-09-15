#  Problem 3:  Biggest and smallest number in an array
#  Write a program to print the biggest and smallest number in the array. 

# Input: arr[] = {1, 2, 3, 4, 5}
# Output: Maximum is: 5
# Minimum is: 1

# Input: arr[] = {5, 3, 7, 4, 2}
# Output: Maximum is: 7
# Minimum is: 2

def main(arr:list):
    print(f"Maximum is: {max(arr)}")
    print(f"Minimum is: {min(arr)}")
    
    # or 

def find_max_min(arr):
    if len(arr) == 0:
        print("Array is empty")
        return

    max_num = arr[0]
    min_num = arr[0]

    for num in arr:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num

    print("Maximum is:", max_num)
    print("Minimum is:", min_num)
    
if __name__ == "__main__":

    arr1 = [1, 2, 3, 4, 5]
    arr2 = [5, 3, 7, 4, 2]

    find_max_min(arr1)
    find_max_min(arr2)
