# Ex3 - String
# Enter text and check if it contains capital letter or not
# Display "Yes" if capital
# display "No" if all lowercase letter
text=input("Enter text : ")
isContains=False
for i in range(len(text)):
    if text[i]==text[i].upper():
        isContains=True
if isContains:
    print("Yes")
else:
    print("No")
