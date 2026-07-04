#program on given word is vowel word or not a vowel
#Ex-7
word=input("Enter a word:")
for ch in word:
    res="NOT VOWEL WORD"
    if(ch in "aeiouAEIOU"):
        res="VOWEL WORD"
        break
print("{} IS {}".format(word,res))