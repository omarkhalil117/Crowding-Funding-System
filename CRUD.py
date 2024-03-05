from datetime import datetime

def getAll():

    with open('projects.txt' , 'r') as rs:
        for line in rs:
            print(line.strip())

def addProject(email):

    title = input("Enter title")
    if( len(title) == 0):
        print("Empty field")
        return
    
    details = input("Details")
    if( len(details) == 0):
        print("Empty field")
        return
    
    totalTarget = input("Enter Total target")
    try:
        int(totalTarget)
    except:
        print("Target is not a number")
        return

    startDate = input("Enter start Date format: YYYY-MM-DD \n")
    endDate = input("Enter end Date format: YYYY-MM-DD \n")

    try:
        startDate = datetime.strptime(startDate,"%Y-%m-%d")
        endDate = datetime.strptime(endDate,"%Y-%m-%d")
    except ValueError:
        print("Invalid date")
        return
        
    project = f'{email}:{title}:{details}:{totalTarget}:{startDate}:{endDate}\n'

    with open('projects.txt','w') as rs:
        rs.write(project)

def deleteProject(email,title):
    flag = 0
    with open('projects.txt','r') as rs:
        lines = rs.readlines()
    with open('projects.txt','w') as ws:
        for line in lines:
            project = line.strip().split(':')
            if project[0] == email and project[1] == title:
                flag = 1
            else:
                ws.write(project)

    if flag != 1:
        print("Project got deleted")
    else:
        print("Project not found or you are not authorized")

def editProject(email,selector,toEdit,update):
    flag = 0
    with open('projects.txt' , 'r') as rs:
        lines = rs.readlines()
    with open('projects.txt', 'w') as ws:
        for line in lines:
            project = line.strip().split(':')
            if project[0] == email and project[1] == selector:
                project[toEdit] = update
                ws.write(":".join(project))
                print("Edited Successfully")
                flag = 1
            else:
                ws.write(line)
    if flag != 1:
        print("Project not found")



