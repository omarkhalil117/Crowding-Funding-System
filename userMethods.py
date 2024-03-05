import CRUD
from datetime import datetime

def register():
    
    fname = input("Enter your first name\n")
    lname = input("Enter your last name\n")
    
    if( len(fname) == 0 or len(lname) == 0 ):
        print("Empty firstname or lastname")
        return

    email = input("Enter your email\n")

    if( len(email.split('@')) != 2):
        print("Invalid email")
        return

    password = input("Enter your password\n")

    if( len(password) < 8):
        print("Password is too short")
        return

    confirm = input("Confirm password\n")
    
    if( password != confirm):
        print("Passwords doesn't match or ")
        return

    phone = input("Enter your phone number [Egyptian numbers only\n")

    if( len(phone) != 11 or phone[0:3] not in ["010","011","012","015"]):
        print("Invalid number")
        return
    
    user = f'{fname}:{lname}:{email}:{password}:{phone}'

    with open('users.txt', 'w') as ws :
        ws.write(user)


def login():

    email = input("Enter email\n")
    if( len(email) == 0 ):
        print("Empty field")
        return

    password = input("Enter password\n")
    if( len(password) == 0 ):
        print("Empty field")
        return
    
    flag = 0

    with open('users.txt','r') as rs:
        lines = rs.readlines()

        for line in lines :
            user = line.strip().split(':')
            if user[2] == email and user[3] == password :
                flag = 1
                break

    if flag != 1 :
        print("Wrong email or password")
        return
    
    while(True):
        userChoice = int(input("1) See all projects\n2) Add project\n3) Edit project\n4) Delete project\n5) Exit\n"))

        if(userChoice == 1):
            CRUD.getAll()

        elif(userChoice == 2):
            CRUD.addProject(email)

        elif(userChoice == 3):
            try:
                toEdit = int(input("1) Edit title\n2) Edit details\n3) Edit total target\n4) Edit start date\n5) Edit end date\n"))
            except ValueError:
                print("Wrong Value")
                continue

            if toEdit not in range(1,6):
                print("Wrong input")
            else:
                
                selector = input("Enter title of project you want to edit")

                if len(selector) == 0:
                    print("Empty field")
                    continue

                if toEdit == 1:
                    update = input("Enter new Title\n")
                    if len(update) == 0:
                        print("Empty field")
                        continue

                elif toEdit == 2:
                    update = input("Enter new details\n")
                    if len(update) == 0:
                        print("Empty field")
                        continue                   

                elif toEdit == 3:
                    try:
                        update = int(input("Enter new total target\n"))
                    except ValueError:
                        print("wrong input not a number")
                        continue
                    
                elif toEdit == 4 or toEdit == 5:
                    try:
                        update = input("Enter new Date format: YYYY-MM-DD \n")
                        update = datetime.strptime(update,"%Y-%m-%d")
                    except ValueError:
                        print("Invalid date")
                        continue
                
                CRUD.editProject(email,selector,toEdit,update)

        elif(userChoice == 4):
            title = input("Enter project title\n")
            if( len(title) == 0):
                print("Error Empty field")
            else:
                CRUD.deleteProject(email,title)

        elif(userChoice == 5):
            break

        else:
            print("Wrong choice")

