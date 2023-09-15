#  Problem 2:  Determine whether a given string is Palindrome
#  A string “madam” is a palindromic string because it reads the same forwards and backward. 
# Input: “anna”
# Output: true

# Input: “India”
# Output: false


def main(string:str):
    if string == string[::-1]:
        return True
    return False

if __name__ == "__main__":
    print(main("madam"))
    print(main("India"))
    print(main("anna")) 