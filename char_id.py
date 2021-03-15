c=input("Enter a character")
if c>='a' and c<='z':
    print("Lower case")
elif c>='A' and c<='Z':
    print("Upper case")
elif c>='0' and c<='9':
    print("Digit")
else:
    print("Special character")
