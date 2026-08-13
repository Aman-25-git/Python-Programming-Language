#Renaming file name by help od os
#OsRenameFile.py
import os
try:
    os.rename("Magic\\mainpy.py","Magic\\same.py")
    print("File Named Renamed--Verify")
except FileNotFoundError:
    print("File Does Not Exist")