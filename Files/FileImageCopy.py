#Program to copy a image to another file
#FileImagecopy.py
with open("c:\\Users\\USER\\Documents\\aman.png.jpeg","rb") as rp:
    with open("amancopy.png","wb") as wp:
        srcfile=rp.read()

        wp.write(srcfile)
    print("1 Image is copied----verifiy")
