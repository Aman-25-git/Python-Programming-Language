#program to define PureKeywordvariableLengthArgs
#Ex-2
def totmarks(sno,sname,cls,*intmarks,city="Madras",**submarks):
    print("-"*50)
    print("\tSno:", sno)
    print("\tSname:", sname)
    print("\tClass:", cls)
    print("\tIntmarks:", format("No internal marks are there for this student" if len(intmarks)==0 else intmarks))
    print("\tCity:", city)
    print("\tSubmarks:", submarks)
    print("-"*50)
    s=0
    for val in submarks.values():
        s=s+val
    print("\tTotal Marks:",s)
    print("-" * 50)

#Main Program
totmarks( 10, "RS",10,20,30,40,50,t=56,h=90,m=90,s=89,so=78 )
totmarks( 100, "TR", "Inter",2,3,5,6,m=90,p=89,c=67)
totmarks( 102,"Harika","B.Tech",OS=50,DBMS=60,NW=50)
totmarks(103,"Ramesh","Degree",java=78,py=89,c=89)
totmarks(123,"SAMBA","Phd",city="MAYANMAR",psco=567)

#Function defining with final function syntax
#i.e, def functionname(list of pos args,*variablelength,Default params,**keywordvarlen):
#   ---------
#   --------
