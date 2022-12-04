def nameRank(names, marks, updates,n):
    print("mark obtain by student :-----")
    print("                       ")
    def ranking(names,marks,n): #function for ranking student
        print("student","    ","mark","  ","rank")
        print("===================================")
        l=[]
        l2=[]
        for i in range(n):
            l.append(marks[i])
            x=sorted(l,reverse=True)    
        for i in x:
            l2.append(l.index(i))
        for i in range(n):
            print(names[l2[i]],"--> ",x[i],"    ",i+1)
    
    ranking(names,marks,n)
    print("----------------------------------")
    print("mark jump by student :-----")
    print("                     ")
    for i in range(n):
        print(names[i],"-->",updates[i])
    print("----------------------------------")
    print("mark obtain after update by student :-----")
    print("                     ")
    for i in range(n):
        marks[i]+=updates[i]
    ranking(names,marks,n)




# Names of the students
names= ["Ram", "Rohan", "Ankit"]

# Marks of the students
marks = [80, 71, 75]

# Updates that are to be done
updates = [0, 5, -9]

# Number of students
n = len(marks)

nameRank(names, marks, updates, n)

