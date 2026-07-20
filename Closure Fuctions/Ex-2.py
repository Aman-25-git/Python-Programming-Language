#program to demonstrate closure function
#Ex-1
def grandparents(gpassets=100):
    print("Grandparents assests=", gpassets)
    def grandchild(gca):
        tatass=gpassets+gca
        print("\tgrandchild()--Grand Parent Property:{}  Child Property:{}   totprop:{}".format(gpassets,gca,tatass))
    return grandchild
#Main Program
grc=grandparents()
for gca in range(1000,1021):
    grc(gca)