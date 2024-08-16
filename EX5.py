# Ex5 - String 
# We have text = "454639"
# Q1 - Count odd and even number in text
# Q2 - Sum all number 
# Q3 - Sum only even number 
# Q4 - Reverse
# Q1 Count odd and even number in text
# text="454639"
# count_even=0
# count_odd=0
# for i in range(len(text)):
#     if int(text[i])%2==0:
#         count_even+=1
#     elif int(text[i])%2==1:
#         count_odd+=1
# print("number even is :",count_even)
# print("number odd is :",count_even)
# Q2 Count odd and even number in text
# text="454639"
# sum=0
# for i in range(len(text)):
#     sum+=int(text[i])
# print(sum)
# Q3 Sum only even number 
# text="454639"
# sum=0
# for i in range(len(text)):
#     if int(text[i])%2==0:
#         sum+=int(text[i])
# print(sum)
# Q4 Reverse
text="454639"
for i in range(len(text)):
    print(text[len(text)-1-i])



