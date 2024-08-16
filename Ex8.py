# Ex8 - String
# We have text = "9394884039"
# Q1 - How many number 8 in string
# Q2 - What is first index of letter 8
# Q1
# text="9394884039"
# sum=0
# for i in range(len(text)):
#     if int(text[i])==8:
#         sum+=1
# print(sum)
#Q2
text="89394884039"
sum=0
first_index=False
for i in range(len(text)):
    if int(text[i])==8 and not first_index:
        print(i)
        first_index=True

        
