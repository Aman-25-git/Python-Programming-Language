#program to demonstrate closure function
#Ex-1
def grandparents(gpassets=100):
    print("Grandparents assests=", gpassets)
    def grandchild():
        print("grandchild()--->Grandchild assests=", gpassets)
    return grandchild
#Main Program
grc=grandparents()
grc()
grc()
grc()