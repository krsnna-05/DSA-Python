class Solution:
    def printNumber(self):

        n = int(input("Enter Your Number : "))

        if -1000 < n < 1000:
            print(f"The Number is {n}")
        else:
            print("Then Nuber should be in -1000 to 1000")
          
s = Solution()

s.printNumber()