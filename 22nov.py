"""#class membersship test
class A():
    pass
class B():
    pass
class C():
    pass
a=A()
b=B()
c=C()
print(isinstance(a,A))
print(isinstance(b,B))
print(isinstance(a,C))
"""

names=list(map(str,input("Names: ").split(",")))
marks=list(map(int,input("Marks: ").split(",")))
update=list(map(int,input("Update: ").split(",")))

#calculating marks after updation
for i in range(len(marks)):
    marks[i]=marks[i]+update[i]

#printing the name of the student with maximum marks
print(names[marks.index(max(marks))],"got maximum marks:",max(marks))

#calculating and printing the rank of the students
rank=sorted(marks,reverse=True)
for i in range(len(marks)):
    print(names[marks.index(rank[i])],"got",i+1,"rank:",rank[i])
