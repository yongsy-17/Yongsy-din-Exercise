# Ex9 - String
# We have string = "3 4 5 6"
# Q1 - Remove space and keep result = "3456"
# Q2 - Multiple each letter by 2 result = "6 8 10 12"
# number="3 4 5 6"
# result=""
# for i in range(len(number)):
#     if number[i]!=" ":
#         result+=number[i]
# print(result)
# Q2
number="3 4 5 6"
result=""
result1=""
for i in range(len(number)):
    if number[i]!=" ":
      result=int(number[i])*2
      result1+=str(result)+str(" ")
print(result1)
   