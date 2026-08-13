#Program to copy music form onr file to another
#FileMusiccopy.py
with open("C:\\Users\\USER\\OneDrive\\Pictures\\paulyudin-no-copyright-music-482400.mp3","rb") as rp:
    with open("amanmusic.mp3","wb") as wp:
        srcfile=rp.read()

        wp.write(srcfile)
    print("1 Music is copied----verifiy")
