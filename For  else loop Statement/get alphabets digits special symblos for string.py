#program to get the special symbols and dits and alphabets form an string
#Ex-13 home work
s = input("Enter a string: ")

alphabets = ""
digits = ""
special_symbols = ""

for ch in s:
    if ch.isalpha():
        alphabets = alphabets + ch
    elif ch.isdigit():
        digits =digits + ch
    else:
        special_symbols += ch

print("Alphabets :", alphabets)
print("Digits :", digits)
print("Special Symbols :", special_symbols)
