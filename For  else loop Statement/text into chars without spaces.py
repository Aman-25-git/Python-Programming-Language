#Program for accepting a Line of Text and Find Number chars without spaces
# (Dont use len() )
#Ex-8
word=input("Enter a word/line of text:")
l=0
nfc=0
for x in word:
    if not x.isspace():
        l=l+1
    else:
        nfc=nfc+1
else:
    print("\tGiven String = {}".format(word))
    print("Length Given String without Spaces=", l)
    print("Number of Spaces=", nfc)
    print("Number of Characters With spaces:{}".format(nfc+l))