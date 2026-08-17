##Program to declare common object for all instance datamembers
#ClassLevelDataMemberEx-2.py
class Student:
    pass
#main program
Student.city="Ahmedhabad"
Student.crs="Java Full Stack"
print(Student.city)
print(Student.crs)