#Program for Demonstrating the Concept of Closure
#Ex-4
gpassets1=10
def garndparents():
    gpassets2=100
    print("Grand parents prop:{}".format(gpassets2))
    def grandchild(gcp):
        nonlocal gpassets2
        global gpassets1
        totprop=gpassets1+gpassets2+gcp
        print("grandchild()--Grand Grand Prop:{} :Grand PP:{}  Child Prop:{}   totprop:{}".format(gpassets1,gpassets2,gcp,totprop))
        gpassets1=gpassets1+1
        gpassets2=gpassets2+1
    for gcp in range(1000,1011):
        grandchild(gcp)

#main program
garndparents()