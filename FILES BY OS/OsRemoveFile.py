#removing an file with help of an os
#OsRemoveFile.py
import os
try:
    os.remove("Scam\\Scams.data")
    print("File Removed--Verify")
except FileNotFoundError:
    print("File Does Not Exist")
