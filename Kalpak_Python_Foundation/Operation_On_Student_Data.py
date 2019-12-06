

# students  data
student=[(111,"kalpak","kalpakmalpe4@gmail.com","python","true",{"initial":20, "mid":30, "final":40 }) ,
         (112,"harshad","harshadpatil@gmail.com","python","true",{"initial":20, "mid":30, "final":30 }),
         (113,"mayur","mayurkasture94@gmail.com","python","true",{"initial":10, "mid":10, "final":40 }),
        (114,"akash","akash@gmail.com","java","true",{"initial":10, "mid":10, "final":10 }),
         (115,"akshay","akshay@gmail.com","java","false",{"initial":10, "mid":30, "final":10 })
         ]


# 1.display all students

def display():
    for stud in student:
        print(stud)


# 2. to get the result of all students

def getresult():

    for stud in student:
        total=stud[5]["initial"]+stud[5]["mid"]+stud[5]["final"]
        print("Test result of",stud[1],"is",total)

# 3. display all the student of given course
def getcourse():
    for stud in student:
        if stud[3] == "python":
            print(stud[1],"with course",stud[3])


# 4.find course wise toppers


def gettoppers(course):
    maxmarks=0
    maxpos=0
    i=0;

    for stud in student:

        if(stud[3] == course):
             tot=stud[5]["initial"]+stud[5]["mid"]+stud[5]["final"]

             if (tot > maxmarks):
                 maxmarks=tot
                 maxpos=i
        i += 1

    print("topper in",course,"is:",student[maxpos])




# 5.display all active students
def getactive():
    for stud in student:
        if stud[4] == "true":
            print(stud[1],"is Active Student..")

# 6.Count no. of students with each course

def cntstd(course):
    a = [x for x in student if x[3] == course]
    # print (a)
    print("Number of students in ",course," is : ", len(a))

'''num=0
    count=0
    i=0
    for stud in student:
        if(stud[3]==course):
            tot=stud[0]
            print (len(tot))
            #print(tot)
            if(tot>num):
                num=tot
                count=count+1
                num=num//10

            print((count))

     '''




# 7.course with highest no of students
def highest():
    '''for stud in student:
        if (stud[3]=="python"  > stud[3]=="java"):
            print("Python Has Highest Students")
        else:
            print("java Has Highest Students")
     '''

    python = [x for x in student if x[3] == "python"]
    a=(len(python))

    java = [x for x in student if x[3] == "java"]
    b=(len(java))

    if a > b:
            print("Python has Higher Students..")
    else:
            print("JAVA has Higher Students..")





# calling the function

display()

getresult()

getcourse()

gettoppers("python")

getactive()

cntstd("java")

highest()



















































'''import numpy as np

dtypes = [('rollno',int),('name', 'S10'), ('email','S30'), ('course', 'S10'),('status','S10',{})]

# Values to be put in array
values = [(111,"kalpak","kalpakmalpe4@gmail.com","python","true"),]

# Creating array
arr = np.array(values, dtype = dtypes)
print(arr)
'''