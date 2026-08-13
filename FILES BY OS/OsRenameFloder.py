#Renaming the floder eith help of an os
#OsRenameFloder.py
import os
try:
    os.rename("Scam","Magic")
    print("Folder Renamed--Verify")
except FileNotFoundError:
    print("File Does Not Exist")