# Input Output
# Subscribe to TUF+

# Hints
# Company
# Complete the function printNumber which takes an integer input from the user and prints it on the screen.



# Use:-

# for C++ : cout << variable_name;
# for Java : System.out.print();
# for Python : print()
# for Javascript : console.log()

# Example 1

# Input(user gives value): 7

# Output: 7

# Example 2

# Input(user gives value): -5

# Output: -5

class Solution:
    def printNumber(self):

        n = int(input("Enter Your Number : "))

        if -1000 < n < 1000:
            print(f"The Number is {n}")
        else:
            print("Then Nuber should be in -1000 to 1000")
          
s = Solution()

s.printNumber()