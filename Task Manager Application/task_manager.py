# =====importing libraries===========
from datetime import date  # This will be used to get the date
import re  # This will be used to separate a list

# ====Login Section====
with open('user.txt', 'r+') as f1:
    # I am opening this file in r+ as I do not need to overwrite information nor append it
    Username = ""  # This variable will hold the username input from the user
    Password = ""  # This variable will hold the password input from the user
    details = ""  # This variable will hold the login details from the user.txt file
    for lines in f1:  # This for loop is to gather the information from the "user.txt" file
        details += lines
    correct_details = details.replace(",", "")  # I am removing all commas from the string
    login_details = correct_details.split()
    # I am splitting the string into a list,so we can pick username or password
    f1.close()  # closing the file once I have used it

    # ====Login Section for the Admin====

    # I have created a while loop which will not allow the user login unless they are the admin as it triggers a
    # different menu.
    # As we know the location of the admin login details, we can use it to make the condition on the while loop
    # to trigger the menu.
    while Username != login_details[0]:
        Username = str(input("Enter the username: "))
        if Username == login_details[0]:
            Password = str()
            while Password != login_details[1]:
                Password = str(input("Enter your password: "))
                if Password != login_details[1]:
                    print("Incorrect password!\nTry again.\n")
                elif Password == login_details[1]:

                    # =====menu section for admin===========

                    # This is a different user interface than the normal user menu.
                    # It allows the admin to register new users and shows the statistics
                    while True:
                        menu = input('''Select one of the following Options below:
                                    r - Registering a user
                                    a - Adding a task
                                    va - View all tasks
                                    vm - view my task
                                    s - statistics
                                    e - Exit
                                    : ''').lower()
                        if menu == 'r':  # This option allows the admin to register a new user
                            pass
                            with open('user.txt', "a+") as f2:
                                # we are opening it in a+ as we want to add the login details without deleting any
                                # previous information.
                                NewUser_Username = str(input("Enter the username: "))
                                # The variable "NewUser_Username" will hold the username input from the user.
                                NewUser_Password = str(" ")
                                # The variable "NewUser_Password" will hold the password input from the user.
                                NewUser_Password_Confirmation = str()
                                # The variable "NewUser_Password_Confirmation" will make the user confirm their
                                # password.
                                # The while loop below is there to ensure the users password is confirmed.
                                # If the password does not match after they enter it in for the second time,
                                # the user will have to enter them both in until they get it correct.
                                while NewUser_Password != NewUser_Password_Confirmation:
                                    NewUser_Password = str(input("Enter your password: "))
                                    NewUser_Password_Confirmation = str(input("Confirm your password: "))
                                    if NewUser_Password != NewUser_Password_Confirmation:
                                        print("The two passwords do not match, please re-enter them")
                                    else:
                                        # Once the password matches, it will add the login details to 'user.txt'.
                                        f2.write(f"\n{NewUser_Username}, {NewUser_Password}")
                                        f2.close()
                                        print("Thank you for entering your details!"
                                              "\nThey have been added to our system!")
                        elif menu == 'a':  # This option is to add a task to the list of tasks.
                            pass
                            with open('tasks.txt', "a+") as f3:
                                # we are opening it in a+ as we want to add the login details without deleting any.
                                # previous information The variables below will be there to collect the necessary.
                                # information from the user to add into the "tasks.txt" file.
                                Add_task_Username = input("What is your username: ")
                                Task_title = input("Enter the title of the task: ")
                                Description_Task = input("Enter a description of the task: ")
                                Due_Date = input("Enter the due date in \"dd mmm yyyy\" format: ")
                                Task_completed = input("Has the task been completed? Yes or No? ")
                                today = date.today()
                                Today = today.strftime(
                                    "%d %b %Y")  # This variable will automatically input today's date.
                                f3.write(f"\n{Add_task_Username}, {Task_title}, {Description_Task}, "
                                         f"{Today}, {Due_Date},{Task_completed}")
                                f3.close()

                        elif menu == 'va':  # This option is to view all the tasks.
                            pass
                            with open('tasks.txt', "r+") as f4:
                                # I am opening this file in r+ as I do not need to overwrite information nor append it.
                                i = 0  # This variable is going to be used in a for loop to get the appropriate task
                                # title.
                                t = 0  # This variable is going to be used in a for loop to get the appropriate task
                                # description.
                                tasks_viewer = ""  # This variable will hold the information from the "tasks.txt" file
                                for lines in f4:
                                    # This for loop is to gather the information from the "tasks.txt" file.
                                    tasks_viewer += lines
                                all_tasks = tasks_viewer
                                all_tasks_final = re.split(r'[,\n]', all_tasks)
                                # I am using the re.split to remove multiple delimiters at once.
                                # In this case, I am removing commas and \n.
                                for i in range(1, len(all_tasks_final), 6):  # This for loop will ensure that the task
                                    # title and task description match.
                                    for t in range(2, len(all_tasks_final), 6):
                                        if i + 1 == t:
                                            print(f"Task Title: {all_tasks_final[i]}\nTask Description:"
                                                  f"{all_tasks_final[t]}\n")
                                            f4.close()

                        elif menu == 'vm':  # This option will show all tasks associated to the user who logged in.
                            pass
                            with open('tasks.txt', "r+") as f5:
                                # I am opening this file in r+ as I do not need to overwrite information nor append it.
                                i = 0  # This variable is going to be used in a for loop to get the appropriate task
                                # title.
                                t = 0  # This variable is going to be used in a for loop to get the appropriate task
                                # description.
                                n = 0  # This variable is going to be used in a for loop to get the appropriate username
                                tasks_viewer2 = ""  # This variable will hold the information from the "tasks.txt" file.
                                for lines in f5:
                                    # This for loop is to gather the information from the "tasks.txt" file.
                                    tasks_viewer2 += lines
                                my_tasks = tasks_viewer2
                                my_tasks_final = re.split(r'[,\n]', my_tasks)
                                # I am using the re.split to remove multiple delimiters at once.
                                # In this case, I am removing commas and \n.
                                for n in range(0, len(my_tasks_final), 6):
                                    # This for loop will ensure that the username, task title, and task description
                                    # match.
                                    if my_tasks_final[n] == Username:
                                        for i in range(1, len(my_tasks_final), 6):
                                            for t in range(2, len(my_tasks_final), 6):
                                                if n + 2 == i + 1 == t:
                                                    print(f"Username: {my_tasks_final[n]}\nTask Title"
                                                          f":{my_tasks_final[i]}."
                                                          f"\nTask Description: {my_tasks_final[t]}.\n")
                                                    f5.close()

                        elif menu == 's':  # This is option will show the statistics.
                            pass
                            with open('tasks.txt', "r+") as f6:
                                # I am opening this file in r+ as I do not need to overwrite information nor append it.
                                tasks_viewer3 = ""  # This variable will hold the information from the "tasks.txt" file.
                                for lines in f6:
                                    # This for loop is to gather the information from the "tasks.txt" file.
                                    tasks_viewer3 += lines
                                all_tasks2 = tasks_viewer3
                                all_tasks_final2 = re.split(r'[,\n]', all_tasks2)
                                # I am using the re.split to remove multiple delimiters at once.
                                # In this case, I am removing commas and \n.
                                print(f"Total numbers of tasks: {len(all_tasks_final2[0:len(all_tasks_final):6])}\n"
                                      f"Total number of users: {len(login_details[0:len(login_details):2])}")

                        elif menu == 'e':  # This option is to end the program
                            print('Goodbye!!!')
                            exit()

                        else:
                            print("You have made a wrong choice, Please Try again")

        # ====Login Section for the other users====

        elif Username not in login_details[2:len(login_details):2]:
            print("Incorrect username!\nTry again.\n")
        elif Username in login_details[2:len(login_details):2]:
            # As there are multiple users that can be added,
            # I want to ensure that it would always capture the username added.
            # As we know that the "user.txt" file will go "username, password" and
            # that the first location of the first username registered will be 2 (that is not admin)
            # and it will go in steps of 2.
            Password = str()
            while Password != login_details[3:len(login_details):2]:
                Password = str(input("Enter your password: "))
                if Password not in login_details[3:len(login_details):2]:
                    print("Incorrect password!\nTry again.\n")
                elif Password in login_details[3:len(login_details):2]:

                    # =====menu section for the other users===========
                    # This is the same code for the admin menu, it is just missing the register and statistics option

                    while True:
                        menu = input('''Select one of the following Options below:
                                    a - Adding a task
                                    va - View all tasks
                                    vm - view my task
                                    e - Exit
                                    : ''').lower()
                        if menu == 'a':
                            pass
                            with open('tasks.txt', "a+") as f3:
                                Add_task_Username = input("What is your username: ")
                                Task_title = input("Enter the title of the task: ")
                                Description_Task = input("Enter a description of the task: ")
                                Due_Date = input("Enter the due date in \"dd mmm yyyy\" format: ")
                                Task_completed = input("Has the task been completed? Yes or No? ")
                                today = date.today()
                                Today = today.strftime("%d %b %Y")
                                f3.write(f"\n{Add_task_Username}, {Task_title}, {Description_Task}, "
                                         f"{Today}, {Due_Date},{Task_completed}")
                                f3.close()

                        elif menu == 'va':
                            pass
                            with open('tasks.txt', "r+") as f4:
                                i = 0
                                t = 0
                                tasks_viewer = ""
                                for lines in f4:
                                    tasks_viewer += lines
                                all_tasks = tasks_viewer
                                all_tasks_final = re.split(r'[,\n]', all_tasks)
                                for i in range(1, len(all_tasks_final), 6):
                                    for t in range(2, len(all_tasks_final), 6):
                                        if i + 1 == t:
                                            print(f"Task Title: {all_tasks_final[i]}\nTask Description:"
                                                  f"{all_tasks_final[t]}\n")
                                            f4.close()

                        elif menu == 'vm':
                            pass
                            with open('tasks.txt', "r+") as f5:
                                i = 0
                                t = 0
                                n = 0
                                tasks_viewer2 = ""
                                for lines in f5:
                                    tasks_viewer2 += lines
                                my_tasks = tasks_viewer2
                                my_tasks_final = re.split(r'[,\n]', my_tasks)
                                for n in range(0, len(my_tasks_final), 6):
                                    if my_tasks_final[n] == Username:
                                        for i in range(1, len(my_tasks_final), 6):
                                            for t in range(2, len(my_tasks_final), 6):
                                                if n + 2 == i + 1 == t:
                                                    print(f"Username: {my_tasks_final[n]}\nTask Title"
                                                          f":{my_tasks_final[i]}."
                                                          f"\nTask Description: {my_tasks_final[t]}.\n")
                                                    f5.close()

                        elif menu == 'e':
                            print('Goodbye!!!')
                            exit()

                        else:
                            print("You have made a wrong choice, Please Try again")
