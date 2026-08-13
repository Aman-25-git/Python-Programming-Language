#create a floder by help of os
#OsFloderCreate.py
import os
try:
    os.mkdir("Scam")
    print("Floder is created --verify")
except FileExistsError:
    print(" File dosn't exist")
except FileNotFoundError:
    print("File not Found")