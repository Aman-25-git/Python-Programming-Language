#program for accepting a Line of Text and Convert into Upper Case
# Don't Use Upper()
line=input('Enter a Line of Text:')
print("Given Line=",line)
uc=""
for ch in line:
    if ord(ch) in range(97,123):
        uc=uc+chr(ord(ch)-32)
    else:
        uc=uc+ch
else:
    print("Upper Case Data=",uc)