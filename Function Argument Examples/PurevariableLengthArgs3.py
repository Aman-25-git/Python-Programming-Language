#program to define PurevariableLengthArgs
#Ex-3
def d(sno,sname,marks,*Aman,city="HYD"):
    print(sno,sname,marks)
    print("NO Of Variable length args=",len(Aman))
    s=0
    for val in Aman:
        print(val)
        s=s+val
    print()
    print("Sum = ",s)
#Main Program
d(100,"RS",34.56,10,20,30,40,50)  # Function Call-1
d(200,"DR",33.33,10,20,30,40)  # Function Call-2
d(300,"TR",55.55,10,20,30)  # Function Call-3
d(400,"SR",22.22,10,20)  # Function Call-4
d(500,"KV",44.23,10)  # Function Call-5
d(600,"JH",44.78)  # Function Call-6
#d(800,"PT",21.11,city="RSA",1.2,2.3,3.4)
#This program not going to execte because the position follws keyword agrs(last one)
