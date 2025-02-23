# # TWO-SUM
# class Solution:
#     def two_sum(self, nums, target):
#         for i , num1 in enumerate(nums):
#             for j , num2 in enumerate(nums):
#                 if i != j and num1 + num2 == target:
#                     return [i, j]


# solution = Solution()

# number = list(map(int,input("Enter you nums").split()))

# target = int(input("enter your target num:- "))

# result = solution.two_sum(number, target)

# if result:
#     print("indices",result)
# else:
#     print("Not find")


# # PALINDROME
# class Solution(object):
#     def is_palindrome(self, x):
#         return str(x) == ''.join(reversed(str(x)))
    

# solution = Solution()

# num = 121
# result = solution.is_palindrome(num)
# if result:
#     print(f"okk {result}")
# else:
#     print("Not find")


# # roman to int
# class Solution(object):
#     def romanToInt(self, s):
#         translator = {
#             "I" : 1,
#             "V" : 5,
#             "X" : 10,
#             "L" : 50,
#             "C" : 100,
#             "D" : 500,
#             "M" : 1000
#         }

#         number = 0

#         s = s.replace("IV","IIII").replace("IX","VIIII")
#         s = s.replace("XL","XXXX").replace("XC","LXXXX")
#         s = s.replace("CD","CCCC").replace("CM","DCCCC")

#         for char in s:
#             number += translator[char]
#         return number

# solution = Solution()

# result = solution.romanToInt("MDCMXL")
# print(result)


# class Solution(object):
#     def romanToInt(self, s):
#         translator = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000
#         }

#         number = 0

#         # Replace subtractive notation with equivalent additive notation
#         s = s.replace("IV", "IIII").replace("IX", "VIIII")
#         s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
#         s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

#         # Sum up the values
#         for char in s:
#             number += translator[char]
#         return number

# # Instantiate the Solution class and call the method
# solution = Solution()

# # Test with the Roman numeral "MDCMXL" which means 1640
# result = solution.romanToInt("MDCMXL")
# print(result)




# def main():
#     n = int(input("enter your num? "))
#     for s in sheep(n):
#         print(s)

# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("cow" * i)
#     return flock


# if __name__ == "__main__":
#     main()


# Now using yield 
def main():
    n = int(input("enter your num? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "cow" * i

if __name__ == "__main__":
    main()