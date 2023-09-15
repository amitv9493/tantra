# Problem 1: Program to count occurrences of a given character in a string.

#  Count character 'e' in the below string.
# 	Input "geeksforgeeks". 
# 	Output: 4

# 	Count character '3' in the below string.
# 	Input "abccdefgaa."
# 	Output : 3


def main(str, char):
    count = 0
    for i in str:
        if i == char:
            count += 1
    return count

if __name__ == "__main__":
    print(main("geeksforgeeks","e"))