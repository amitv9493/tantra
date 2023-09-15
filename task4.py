'''Problem 4:  Swap two Strings Without Using any Third Variable
 Input: a = "Hello", b = "World".
Output: Strings after swap: a = World and b = Hello'''

def main(a,b):
    a,b = b,a
    print(f"Strings after swap: a = {a} and b = {b}")
    
if __name__ == "__main__":
    main("Hello","World")