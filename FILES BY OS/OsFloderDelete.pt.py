#Deleting a folder by help of os
#OsFloderDelete.pt
import os
try:
    os.rmdir("Scam")
    print("Folder Deleted--Verify")
except FileNotFoundError:
    print("Folder Not Found")
except OSError:
    print("Ensure the Deleting Folder Must be empty--check Once")