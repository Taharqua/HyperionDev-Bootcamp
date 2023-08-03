# =========== importing libraries ===========
# All libraries were written into the functions, however I am using the date.time library and the re library

# =========== defining functions ===========

def view_all_tasks():
    """This is to view all tasks, it is done by reading all the tasks from tasks.txt file and then formatting the tasks
     and printing them all out."""
    import re

    with open("tasks.txt", "r+") as file:
        tasks_viewer = ""
        for va_lines in file:
            tasks_viewer += va_lines
        all_tasks = tasks_viewer
        all_tasks_final = re.split(r'[,\n]', all_tasks)
        for i in range(1, len(all_tasks_final), 6):
            for t in range(2, len(all_tasks_final), 6):
                if i + 1 == t:
                    print(f"Task Title: {all_tasks_final[i]}\nTask Description:"
                          f"{all_tasks_final[t]}\n")
                    file.close()


def add_tasks():
    """This is to add a task using a series of inputs and then writing on the txt file."""
    from datetime import date
    with open('tasks.txt', "a+") as file:
        username = input("What is your username: ")
        Task_title = input("Enter the title of the task: ")
        Description_Task = input("Enter a description of the task: ")
        Due_Date = input("Enter the due date in \"dd mmm yyyy\" format: ")
        Task_completed = input("Has the task been completed? Yes or No? ").capitalize()
        today = date.today()
        Today = today.strftime("%d %b %Y")
        file.write(f"\n{username}, {Task_title}, {Description_Task}, "
                   f"{Today}, {Due_Date},{Task_completed}")
        print("This task has been added to the task list!")
        file.close()


def reg_user():
    """This is to add a new user using a series of for and while loops"""
    import re
    while True:
        with open('user.txt', "r+") as file:
            username = str(input("Enter the username: "))
            ru_login_details = ""
            entire_usernames_list = []
            for ru_lines in file:
                ru_login_details += ru_lines
            all_login_details_str = ru_login_details
            all_login_details_list = re.split(r'[,\n]', all_login_details_str)
            for i in range(len(all_login_details_list)):
                if i % 2 == 0:
                    entire_usernames_list.append(all_login_details_list[i])
                else:
                    pass
            if username in entire_usernames_list:
                print("Error: This username has already been entered. Please try another.")
                continue
            else:
                password = str(" ")
                password_confirmation = str()
                while password != password_confirmation:
                    password = str(input("Enter your password: "))
                    password_confirmation = str(input("Confirm your password: "))
                    if password != password_confirmation:
                        print("The two passwords do not match, please re-enter them")
                        continue
                    else:
                        file.write(f"\n{username}, {password}")
                        file.close()
                        print("Thank you for entering your details!"
                              "\nThey have been added to our system!")
                        break
            break


def view_my_tasks(username):
    """This is to view the users tasks, giving them an option to view a certain task, view all of their tasks and
    change the completion status of their task"""
    import re
    while True:  # I used a while loop to keep the program on the function until the user requested to exit
        try:
            specific_task = int(input("Which tasks would you like to see?\n"
                                      "To view all of your tasks, enter 0.\n"
                                      "To view a specific task, enter the number of the task.\n"
                                      "To go return back to the menu, enter -1 or lower.\n"
                                      "Enter here: "))
            if specific_task == 0:  # This option will show all the tasks that the user who logged in has.
                # It does it by checking the username that logged in matches the username against the task.
                with open('tasks.txt', "r+") as file:
                    tasks_viewer = ""
                    for vm_lines in file:
                        tasks_viewer += vm_lines
                    my_tasks = tasks_viewer
                    my_tasks_v2 = re.split(r'[,\n]', my_tasks)
                    for n in range(0, len(my_tasks_v2), 6):
                        if my_tasks_v2[n] == username:
                            for i in range(1, len(my_tasks_v2), 6):
                                for t in range(2, len(my_tasks_v2), 6):
                                    if n + 2 == i + 1 == t:
                                        print(f"Task ID Number: {(t + 4) / 6}\n"
                                              f"Username: {my_tasks_v2[n]}\nTask Title"
                                              f":{my_tasks_v2[i]}."
                                              f"\nTask Description: {my_tasks_v2[t]}.\n")
                                        file.close()

            if specific_task >= 1:  # This option will allow the user to check a specific task that they want to see.
                # It does it by ensuring that the username that logged in matches the username against the task.
                # If it does then it will display the task, if not it won't.
                with open('tasks.txt', "r+") as file:
                    tasks_viewer = ""
                    for vm_lines in file:
                        tasks_viewer += vm_lines
                    my_tasks = tasks_viewer
                    my_tasks_v2 = re.split(r'[,\n]', my_tasks)
                    if my_tasks_v2[(specific_task * 6) - 6] == username:
                        print(f"Task ID Number: {specific_task}\n"
                              f"Username: {my_tasks_v2[specific_task * 6 - 6]}\n"
                              f"Task Title: {my_tasks_v2[specific_task * 6 - 5]}."
                              f"\nTask Description: {my_tasks_v2[specific_task * 6 - 4]}.\n")
                        while True:   # If the username aligns with the task ID selected,
                            # it will give the user an option to mark that task as completed.
                            mark_completed = input("Do you want to mark this task as complete? Yes/No? ").lower()
                            if mark_completed == "no":
                                break
                            if mark_completed == "yes":
                                while True:   # If the user wants to mark that task as completed, it will segment the
                                    # change the status to completed by changing the completion status to yes,
                                    # then using enumerate, zip and join, re-formatting the information into the
                                    # correct order before writing it back in the tasks.txt file
                                    with open('tasks.txt', "w+") as completed:
                                        my_tasks_v2[specific_task * 6 - 1] = "yes"
                                        login_names = my_tasks_v2[0:len(my_tasks_v2):6]
                                        task_title = my_tasks_v2[1:len(my_tasks_v2):6]
                                        task_descript = my_tasks_v2[2:len(my_tasks_v2):6]
                                        start_date = my_tasks_v2[3:len(my_tasks_v2):6]
                                        end_date = my_tasks_v2[4:len(my_tasks_v2):6]
                                        completion_status = my_tasks_v2[5:len(my_tasks_v2):6]
                                        for i, t in enumerate(zip(login_names, task_title,
                                                                  task_descript, start_date,
                                                                  end_date, completion_status)):
                                            task_list = [t[0], t[1], t[2], t[3], t[4], t[5]]
                                            final_task_list = ",".join(task_list)
                                            completed.write(f"{final_task_list}\n")
                                        print("This task has now been marked as completed!\n")
                                        break
                                break
                            else:       # If the user doesn't enter yes or no when asked if they want to mark the
                                # task as completed, it will keep telling the user to enter an appropriate response.
                                print("Enter an appropriate response!")
                                continue
                    if my_tasks_v2[specific_task * 6 - 6] != username:  # If the username of the task they are trying
                        # to view doesn't match with the user who logged in. It will not allow the user to view that
                        # specific task.
                        print("\nThis task isn't accessible to you as it isn't under your username.\n")
            if specific_task < 0:   # If the user enters a negative integer, it will take the user back to the main menu
                break
        except ValueError as val_error:  # If a non-integer is entered, it will keep telling the user to enter a valid
            # response.
            print(f"\nThat was not a valid response.\n"
                  f"{val_error}\n"
                  f"Please try again.\n")
        except IndexError as index_error:   # If the task id they enter doesn't exist it will print that message.
            print(f"\nYou have entered a task ID number that does not exist!"
                  f"\n{index_error}\nPlease try again!\n")


def generate_report(username):
    """This function writes two different reports on two separate txt files. One about task statistics and the other
      around user statistics. It does by getting the information from user.txt and tasks.txt and manipulating the
      information"""
    import re
    import datetime

    with open('tasks.txt', "r+") as gr_file:
        gather_data = ""
        for gr_lines in gr_file:
            gather_data += gr_lines
        all_data = gather_data
        all_data_list = re.split(r'[,\n]', all_data)
        completion_status_of_tasks = all_data_list[5:len(all_data_list):6]
        word_counter = {}
        for word in completion_status_of_tasks:
            if word not in word_counter:
                word_counter[word] = 1
            else:
                word_counter[word] += 1

        dates_of_tasks = all_data_list[4:len(all_data_list):6]
        overdue_counter = 0
        today = datetime.datetime.today()
        for g in range(len(completion_status_of_tasks)):
            if completion_status_of_tasks[g] == "No":
                if datetime.datetime.strptime(dates_of_tasks[g], " %d %b %Y") < today:
                    overdue_counter += 1
                else:
                    pass
        # From line 167 to line 189, I was able to get information from tasks.txt, split out the information using
        # the re library, so using for loop and dictionary, I could create a counter for both incomplete and complete
        # tasks.
        # I did the same to create an overdue counter for overdue tasks, however, I also had to use the datetime library
        # to format the information being provided. Once correctly formatted, I will write this in this onto another
        # txt file in the appropriate format.

        with open("task_overview.txt", "w+") as tasks_file:
            tasks_file.write(f"Total numbers of tasks: {len(all_data_list[0:len(all_data_list):6])}\n"
                             f"Total numbers of completed tasks: {word_counter['Yes']}\n"
                             f"Total numbers of incomplete tasks: {word_counter['No']}\n"
                             f"Total number of overdue tasks: {overdue_counter}\n"
                             f"The percentage of overdue tasks: "
                             f"{(overdue_counter / len(completion_status_of_tasks)) * 100}%\n"
                             f"The percentage of incomplete tasks: "
                             f"{(word_counter['No'] / len(completion_status_of_tasks)) * 100}%\n")
            tasks_file.close()

        # I have followed the same steps as the first statistics.
        # To understand the process, read the process on line 190

        usernames = all_data_list[0:len(all_data_list):6]
        task_assigned_counter = 0
        for b in range(len(usernames)):
            if usernames[b] == username:
                task_assigned_counter += 1
            else:
                pass

        task_assigned_completed_counter = 0
        for m in range(len(usernames)):
            if usernames[m] == username:
                if completion_status_of_tasks[m] == "Yes":
                    task_assigned_completed_counter += 1
            else:
                pass

        user_overdue_counter = 0
        for t in range(len(completion_status_of_tasks)):
            if usernames[t] == username:
                if completion_status_of_tasks[t] == "No":
                    if datetime.datetime.strptime(dates_of_tasks[t], " %d %b %Y") < today:
                        user_overdue_counter += 1
                    else:
                        pass

        with open("user_overview.txt", "w+") as user_file:
            user_file.write(f"The total number of tasks assigned to {username}: {task_assigned_counter}\n"
                            f"The percentage of total tasks assigned to {username}: "
                            f"{(task_assigned_counter / len(usernames)) * 100}%\n"
                            f"The percentage of tasks assigned to {username} which are completed: "
                            f"{(task_assigned_completed_counter / task_assigned_counter) * 100}%\n"
                            f"The percentage of tasks assigned to {username} which are incomplete: "
                            f"{(1 - (task_assigned_completed_counter / task_assigned_counter)) * 100}%\n"
                            f"The percentage of incomplete overdue tasks for {username}: "
                            f"{(user_overdue_counter / task_assigned_counter) * 100}%\n")
            user_file.close()


def display_statistics(username):
    """This function is to display statistics about tasks and users. It does this by getting the information
    from two separate txt files. If they do not exist, then it will create them and read out the information"""
    if username == "admin":
        while True:
            try:
                with open("task_overview.txt", "r+") as task_file:
                    task_statistics = ""
                    for task_lines in task_file:
                        task_statistics += task_lines
                    print(task_statistics)
                with open("user_overview.txt", "r+") as user_file:
                    user_statistics = ""
                    for user_lines in user_file:
                        user_statistics += user_lines
                    print(user_statistics)
                    break
            except FileNotFoundError:  # This except error is there incase the file doesn't exist. In that case,
                # it will create it.
                generate_report(username)
                continue


with open('user.txt', 'r+') as f1:
    Username = ""  # This variable will hold the username input from the user
    Password = ""  # This variable will hold the password input from the user
    details = ""  # This variable will hold the login details from the user.txt file
    for lines in f1:  # This for loop is to gather the information from the "user.txt" file
        details += lines
    correct_details = details.replace(",", "")  # I am removing all commas from the string
    login_details = correct_details.split()
    f1.close()  # closing the file once I have used it

    # ====Login Section for the Admin====

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
                    while True:
                        menu = input('''Select one of the following Options below:
                                    r - Registering a user
                                    a - Adding a task
                                    va - View all tasks
                                    vm - view my task
                                    ds - display statistics
                                    gr - generate reports
                                    e - Exit
                                    : ''').lower()
                        if menu == 'r':  # This option allows the admin to register a new user
                            pass
                            reg_user()

                        elif menu == 'a':  # This option is to add a task to the list of tasks.
                            pass
                            add_tasks()

                        elif menu == 'va':  # This option is to view all the tasks.
                            pass
                            view_all_tasks()

                        elif menu == 'vm':  # This option will show all tasks associated to the user who logged in.
                            pass
                            view_my_tasks(Username)

                        elif menu == 'ds':  # This is option will show the statistics.
                            pass
                            display_statistics(Username)

                        elif menu == 'e':  # This option is to end the program
                            print('Goodbye!!!')
                            exit()

                        elif menu == 'gr':
                            pass
                            generate_report(Username)

                        else:
                            print("You have made a wrong choice, Please Try again")

        # ====Login Section for the other users====

        elif Username not in login_details[2:len(login_details):2]:
            print("Incorrect username!\nTry again.\n")
        elif Username in login_details[2:len(login_details):2]:
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
                            add_tasks()

                        elif menu == 'va':
                            pass
                            view_all_tasks()

                        elif menu == 'vm':
                            pass
                            view_my_tasks(Username)

                        elif menu == 'e':
                            print('Goodbye!!!')
                            exit()

                        else:
                            print("You have made a wrong choice, Please Try again")
