#Program for accepting any word and decide whether It is Vowel or consonant
# Ex-3
vc=lambda word:"Vowel Word" if "a" in word.lower() or "e" in word.lower() or \
                               "i" in word.lower() or "o" in word.lower() \
                               or "u" in word.lower() else "Consonant Word"
greet=lambda:"Read Python Well"
#Main Program
word=input("Enter any word:")
x=vc(word)
print(x)
print(greet())