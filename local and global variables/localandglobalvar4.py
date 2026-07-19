#program for Demonstrating the Need of Local and Global Variables
#Ex4.py
def learnai():
    sub="AI"
    print("\tTo Implement {} Based Applications we have to learn {} Lang".format(sub,lang))

def learnml():
    sub="ML"
    print("\tTo Implement {} Based Applications we have to learn {} Lang".format(sub,lang))


#Main program
learnai()
lang="Python"
learnml()
#it throws error because we have to declare the lang value before all function calls

