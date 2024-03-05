# register
# login 
# create project
# read all projects
# user edit project
# user delete project

import userMethods

from datetime import date
print("Welcome to Crowd funding app !!!")


while (True):
    choice = int(input("1) Register\n2) Login\n3) Exit\n"))

    if choice == 1:
        userMethods.register()
    elif choice == 2:
        userMethods.login()
    elif choice == 3:
        break
    else:
        print("Wrong choice")

