'''Problem 5: Swap two numbers without using a temporary variable
 Input:integer a = "10", b = "50".
Output: Strings after swap: a = 50 and b = 10'''

def main(a,b):
    a,b = b,a
    print(f"Strings after swap: a = {a} and b = {b}")
    
    
if __name__ == "__main__":
    main(10,50)