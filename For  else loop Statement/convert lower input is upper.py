#program for accepting a Line of Text and Convert into lower Case
# Don't Use lower()
line=input('Enter a Line of Text:')
print("Given Line=",line)
lc=""
for ch in line:
    if ord(ch) in range(65,92):
        lc=lc+chr(ord(ch)+32)
    else:
        lc=lc+ch
else:
    print("Lower Case Data=",lc)